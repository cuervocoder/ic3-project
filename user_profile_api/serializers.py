from rest_framework import serializers
from user_profile_api import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            'id', 
            'email', 
            'password',
            'first_name', 
            'last_name', 
            'is_active', 
            'is_staff',
            'profile_type',
            'date_created',
            'last_updated'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            profile_type=validated_data['profile_type'],
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)
