from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        '/api/register'      
    ]
    
    return Response(routes)

@api_view(['POST'])
def RegisterView(request):
    serializer = RegisterSerializer(data=request.data)
    
    print(serializer.error_messages)
    if serializer.is_valid() is False:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    serializer.save()
    return Response()