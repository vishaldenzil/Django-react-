from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response



class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            return Response(serializer.data)
        except serializers.ValidationError as error:    
            return Response(error.detail)
                                                                                                                                                                                                          
       
        

class DeploymentOnUserViewSet(viewsets.ModelViewSet):
    queryset = DeploymentOnUserModel.objects.all()
    serializer_class = DeploymentOnUserModelSerializer 

    def create(self, request, *args, **kwargs):
        """overwrite this for extra actions"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
         