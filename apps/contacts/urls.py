"""Contacts urls."""

# Django
from django.urls import path, include

# Views
from apps.contacts import views



urlpatterns = [
    path(
        route='create/',
        view=views.CreateContactAPIView.as_view(),
        name='create'
    )
]
