"""Users view"""

#Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)


class UserLoginAPIView(APIView):
    """User login API View"""
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    
    
    
class UserSignUpAPIView(APIView):
    """User Sign up API View"""
    
    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data     
       
        return Response(data, status=status.HTTP_201_CREATED)