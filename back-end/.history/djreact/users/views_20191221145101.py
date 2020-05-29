from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer



class UserRegistrationView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):                                                                                                                                                                                                 
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        return (ht)
        
         