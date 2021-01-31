"""Contacts serializers."""

# Rest Framework
from rest_framework import serializers

# Django
from django.core.validators import RegexValidator

# Models
from apps.users.models import User
from apps.contacts.models import Contact

# Serialiazers
from apps.users.serializers import UserModelSerializer


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact modol serializer."""

    user = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = Contact
        fields = (
            'name',
            'phone_number',
            'email',
            'user'
        )

class CreateContactSerializer(serializers.Serializer):
    """Create contact serializer.""" 

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    name = serializers.CharField(max_length=30)

    email = serializers.EmailField()

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )

    phone_number = serializers.CharField(validators=[phone_regex])


    def create(self, validated_data):
        """handle contact creation."""
        contact = Contact.objects.create(**validated_data)
        return contact
