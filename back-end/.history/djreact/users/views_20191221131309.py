from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import u



class UserRegistrationView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):  
        logger.info("requested to post details of Organization User Registration")                                                                                                                                                                                                
        request_data = request.data.copy()
        request_data['email'] = request_data['email'].lower()
        request_data['password'] = get_random_string(length=8)
        
        serializer = self.serializer_class(data=request_data)
        
         