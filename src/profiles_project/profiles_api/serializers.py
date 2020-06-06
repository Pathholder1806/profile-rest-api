from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView."""

    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):    #ModelSerializer is used to work with models

    class Meta:
        model = models.UserProfile   #To tell with which model this serializer gonna be used.
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])

        user.save()

        return user
