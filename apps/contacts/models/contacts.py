"""Contacts model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Models 
from apps.users.models import User

class Contact(models.Model):
    """Contact model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


    email = models.EmailField(unique=False)

    def __str__(self):
        return '{} contact of {}'.format(self.name, self.user.username)