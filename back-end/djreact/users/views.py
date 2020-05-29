from .models import User
import datetime
from django.conf import settings
from rest_framework import viewsets
from django.contrib.auth import authenticate, get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer , OrganisationUserLoginSerializer
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler



class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":request.data})

        


class OrganisationUserLoginView(viewsets.ModelViewSet):
    model =User
    serializer_class = OrganisationUserLoginSerializer

    def create(self, request):
        try:
            email = request.data['email'].lower()
            password = request.data['password']
            user = authenticate(username=email, password=password)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            message = 'Login successfull'
            context = {'success': True, 'message': message, 'token': token}
            return Response({"data":context})
        

        except Exception as e:
            context = {'error': str(e), 'success': False, 'message': 'Failed to login.'}
            return  Response({"data":request.data,"error":context})



                                                                                                                                                                                                          
         