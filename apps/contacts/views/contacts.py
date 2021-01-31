"""Contacts views."""

# Rest framework
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework import status, mixins, viewsets

# Serializers
from apps.contacts.serializers import (
    ContactModelSerializer,
    CreateContactSerializer
)

# Models
from apps.contacts.models import Contact

# Permisssions
from apps.contacts.permissions import IsContactOwner
from rest_framework.permissions import IsAuthenticated

class ContactsViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    """Contacts view set handle all the CRUD actions for the contacts"""

    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    serializer_class = ContactModelSerializer

    def get_queryset(self):
        """Restrict list to contact owner list,
        and set query to other actions for a specific contact"""

        queryset = Contact.objects.all()
        if self.action == 'list':
            return queryset.filter(user=self.request.user)

        else:
            return queryset.get(name=self.kwargs['name'], user=self.request.user)

        return queryset

    def get_permissions(self):
        """Assing permissions based on actions."""
        if self.action in ['store',]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated, IsContactOwner]
        return [p() for p in permissions]

    def get_object(self):
        """return specific contact."""
        return get_object_or_404(
            Contact,
            user = self.request.user,
            name=self.kwargs['name'] 
        )


    @action(detail=False, methods=['POST'])
    def store(self, request):
        """Handle contact creation"""

        serializer = CreateContactSerializer(context={'request': request}, data=request.data)
        serializer.is_valid()
        contact = serializer.save()
        data = ContactModelSerializer(contact).data
        return Response(data, status=status.HTTP_201_CREATED)