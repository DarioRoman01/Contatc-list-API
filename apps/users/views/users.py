"""Users views."""

# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from apps.users.serializers import (
    UserModelSerializer,
    UserLoginSerializer,
)


class UserLoginAPIView(APIView):
    """User login API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }  

        return Response(data, status=status.HTTP_200_OK)
