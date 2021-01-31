"""Contacts urls."""

# Django
from django.urls import path, include

# Rest framework
from rest_framework.routers import DefaultRouter

# Views
from apps.contacts import views

# Router settings
router = DefaultRouter()
router.register(r'contacts', views.ContactsViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls))  
]
