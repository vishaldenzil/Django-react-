from .models import User
from rest_framework.generics import CreateAPIView,
from .serializers import UserRegistrationSerializer
from rest_framework import viewsets



class UserRegistrationView():
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):  
        logger.info("requested to post details of Organization User Registration")                                                                                                                                                                                                
        serializer = UserRegistrationSerializer(data=request_data)
        serializer.save()
        