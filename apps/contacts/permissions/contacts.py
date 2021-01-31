"""Contacts permissions."""

# REST Framework
from rest_framework.permissions import BasePermission

# Models
from apps.contacts.models import Contact

class IsContactOwner(BasePermission):
    """Allow access only to the owner of the contact"""

    def has_object_permission(self, request, view, obj):
        """Verify that the user is the owner of the contact."""

        try:
            Contact.objects.get(user=request.user)

        except Contact.DoesNotExist:
            return False

        return True
