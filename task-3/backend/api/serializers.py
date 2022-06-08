from .models import UserData, User
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    apiKey = serializers.CharField(required=True)
    secretKey = serializers.CharField(required=True)

    class Meta:
        model = UserData
        fields = ('username', 'apiKey', 'secretKey')

    def create(self, validated_data):
        user = User.objects.filter(username=validated_data["username"]).get()
        
        
        query = UserData.objects.filter(user=user)
    
        userData: UserData    
        if query.count():
            userData: UserData = query.get()
            userData.apiKey = validated_data["apiKey"]
            userData.secretKey = validated_data["secretKey"]
        else:
            userData = UserData.objects.create(
                user=user,
                apiKey=validated_data["apiKey"],
                secretKey=validated_data["secretKey"]
            )
                    
        userData.save()
        return userData