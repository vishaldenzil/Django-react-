from .models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response



class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request):
        try:
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                return Response({"name"})
        except serializers.ValidationError as error:    
            return Response(error.detail)
                                                                                                                                                                                                          
         