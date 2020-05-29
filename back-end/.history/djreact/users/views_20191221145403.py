from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response



class UserRegistrationView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        try:
             print(request.data)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            return Response(serializer.data)
        except serializers.ValidationError as error:
            context = {'error': get_custom_field_errors(error.detail), 'success': False, 'message': _('Failed to create organisation owner.')}
            logger.error("Failed to create organisation owner, due to:{}".format(context))
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                                                                                          
       
        
         