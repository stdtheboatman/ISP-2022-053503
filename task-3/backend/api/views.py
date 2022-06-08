from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserData, User
from .serializers import UserDataSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def setUserData(request):
    request.data["username"] = str(request.user)
    print(request.data)
    serializer = UserDataSerializer(data=request.data)        
    
    if serializer.is_valid() is False:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    serializer.save()
    return Response("")