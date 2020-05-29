from rest_framework import serializers
from .models import User

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content')
