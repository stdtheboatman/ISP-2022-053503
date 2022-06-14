from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserData, User
from .serializers import UserDataSerializer
from .apps import ApiConfig
from .logic import DataHandlerSingleton

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def setUserData(request):
    request.data["username"] = str(request.user)
    serializer = UserDataSerializer(data=request.data)        
    
    if serializer.is_valid() is False:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    serializer.save()
    return Response("")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    dataHandler = DataHandlerSingleton.getInstance()
    
    user: User = request.user
    userData: UserData = UserData.objects.filter(user=user).get()

    data = ""
    try:
        data = dataHandler.getCurrencyDistribution(userData.apiKey, userData.secretKey)
    except Exception as e:
        return Response(str(e), status=404)
        

    return Response(data)