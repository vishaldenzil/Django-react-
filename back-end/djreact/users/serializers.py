from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    
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
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user


class OrganisationUserLoginSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = ('email', 'password')



        