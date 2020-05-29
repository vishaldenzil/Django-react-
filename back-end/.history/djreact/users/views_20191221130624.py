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

         