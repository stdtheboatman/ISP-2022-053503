from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["username"],
                message="Username must be unique"
            )
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user