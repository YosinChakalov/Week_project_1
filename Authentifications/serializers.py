from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'bio', 'user_id', 'status']
        read_only_fields = ['user_id','status']