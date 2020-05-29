from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer



class UserRegistrationView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):  
        logger.info("requested to post details of Organization User Registration")                                                                                                                                                                                                
        serializer = UserRegistrationSerializer(data=request_data)
        serializer.save()
        