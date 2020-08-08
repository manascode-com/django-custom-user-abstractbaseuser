from rest_framework import serializers
from . models import User

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email','created_at')
        read_only_fields = ('id','email','created_at')