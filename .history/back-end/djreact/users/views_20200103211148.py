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
            serializer = self.serializer_class(data=request.data)
            ipd
            if serializer.is_valid():
                serializer.save()
                return Response({"data":request.data})
        except serializer.ValidationError as error:    
            return Response(error.detail)
                                                                                                                                                                                                          
         