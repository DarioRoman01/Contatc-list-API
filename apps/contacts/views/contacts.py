"""Contacts views."""

# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Serializers
from apps.contacts.serializers import (
    ContactModelSerializer,
    CreateContactSerializer
)
from apps.users.serializers import UserModelSerializer

class CreateContactAPIView(APIView):
    """Create contact API view."""
    
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        serializer = CreateContactSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        data = ContactModelSerializer(contact).data
        
        return Response(data, status=status.HTTP_201_CREATED)
