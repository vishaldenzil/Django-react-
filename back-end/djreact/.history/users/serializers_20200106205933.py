from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ('id','email','first_name','last_name','password')
        extra_kwargs = {
            'password': {
                 'write_only': True,
                 'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ OverWriting default 'create' to use create_user to create a new user
            and save hashed password and return a new Profile User """
        
        user = User.objects.create_user(
           email = 
        )
        return user


        