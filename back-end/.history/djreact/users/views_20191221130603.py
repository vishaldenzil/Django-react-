class OrganisationUserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    model = OrganisationUser
    queryset = OrganisationUser.default_manager.all()
    serializer_class = OrganisationUserRegistrationSerializer

    def post(self, request):  
        logger.info("requested to post details of Organization User Registration")                                                                                                                                                                                                
        try:
            # To allow registrations only for only one organisations owner from this API.
            # Others users in the organisation will be added only by the authenticated users.
            if self.get_queryset():
                raise SuspiciousOperation(_('Self signup registrations are closed for this organisation'))

            request_data = request.data.copy()
            request_data['email'] = request_data['email'].lower()
            request_data['password'] = get_random_string(length=8)
            
            serializer = self.serializer_class(data=request_data)

            if serializer.is_valid():
                # Opening new transaction with context manager to make atomic_requests only.
                with transaction.atomic():

                    user_obj = serializer.save()

                    signals.organisations_groups_permissions_setup.send(sender=None, tenant=request.tenant, user=user_obj)
                    

                    # Adding the Organisation user to Owner group
                    owner_group = Group.objects.filter(name='Owner').first()
                    user_obj.groups.add(owner_group)

                    # Creating Internal User with defailt email ID and password
                    ezedox_admin_email = str(request.tenant.schema_name) + '@ezedox.com'
                    ezedox_admin_password = get_random_string(length=8)
                    ezedox_admin_obj = InternalUser.objects.create_superuser(email= ezedox_admin_email,password=ezedox_admin_password)

                    # TODO exception handling for Process Engine Calls
                    # Creating Flowable User for Organisation Owner
                    engine_url = OrganisationLicense.objects.get(organisation=request.tenant)
                    url = CREATE_USER.format(engine_url.processengine)
                    req_body = {}
                    user_id = get_tenant(request) + "_" + user_obj.email
                    # userId encoding
                    req_body["id"] = base64.b64encode(bytes(user_id, 'utf-8')).decode("utf-8")
                    req_body["firstName"] = user_obj.first_name
                    req_body["lastName"] = user_obj.last_name
                    req_body["displayName"] = user_obj.first_name + " " + user_obj.last_name
                    req_body["email"] = user_obj.email
                    req_body["tenantId"] = get_tenant(request)
                    req_body["password"] = password_hash(user_obj.email)
                    
                    action = requests.post(url, auth=(PROCESS_ENGINE_USER, PROCESS_ENGINE_PASSWORD), data=json.dumps(req_body), headers={'Content-Type': "application/json"})

                    #Get Privileges id for modeler access
                    url = GET_PRIVILEGES.format(engine_url.processengine)
                    action = requests.get(url, auth=(PROCESS_ENGINE_USER, PROCESS_ENGINE_PASSWORD))
                    for privilege in action.json()["data"]:
                        if privilege["name"] == "access-modeler":
                            privilege_id = privilege["id"]
                            break
                    
                    #Add privileges For users to access modeler
                    url = ADD_PRIVILEGES.format(engine_url.processengine, privilege_id)
                    req_body = {}
                    req_body["userId"] = base64.b64encode(bytes(user_id, 'utf-8')).decode("utf-8")
                    action = requests.post(url, auth=(PROCESS_ENGINE_USER, PROCESS_ENGINE_PASSWORD), data=json.dumps(req_body), headers={'Content-Type': "application/json"})

                    # Sending emails after successful user creation
                    email_confirm = send_account_activation_email(request, user_obj)                    
                    ezedox_admin_email_confirm = send_ezedox_activation_email(request, ezedox_admin_obj, ezedox_admin_password)

                    #creating a default portal after successfull owner creation
                    create_default_content_and_portal_and_associate()
                context = {"success": True, "message": _("Organisation owner registration completed successfully. Activation link is sent to email."), "data": serializer.data}
                logger.info("Organisation owner registration completed successfully. Activation link is sent to email")
                return Response(context, status=status.HTTP_200_OK)
            context = {'error': get_custom_field_errors(serializer.errors), 'success': False, 'message': _('Failed to create organisation owner.')}
            logger.error("Failed to create organisation owner, due to:{}".format(context))
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except serializers.ValidationError as error:
            context = {'error': get_custom_field_errors(error.detail), 'success': False, 'message': _('Failed to create organisation owner.')}
            logger.error("Failed to create organisation owner, due to:{}".format(context))
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': _('Failed to create organisation owner.')}
            logger.exception("Failed to create organisation owner, due to: {}".format(error))
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)