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
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )
        return user



 from rest_auth.registration.serializers import RegisterSerializer
    class CustomRegisterSerializer(RegisterSerializer):

        email = serializers.EmailField(required=True)
        password1 = serializers.CharField(write_only=True)
        name = serializers.CharField(required=True)
        date_of_birth = serializers.DateField(required=True)

        def get_cleaned_data(self):
            super(CustomRegisterSerializer, self).get_cleaned_data()

            return {
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'name': self.validated_data.get('name', ''),
                'date_of_birth': self.validated_data.get('date_of_birth', ''),
            }

    class CustomUserDetailsSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('email','name','date_of_birth')
            read_only_fields = ('email',)