from rest_framework import serializers
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','first_name']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],first_name=validated_data['first_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user