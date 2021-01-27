"""Users admin."""

# Django
from django.contrib import admin

# Models 
from apps.users.models import User

admin.site.register(User)


