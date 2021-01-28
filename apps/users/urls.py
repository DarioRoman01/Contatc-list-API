"""Users urls."""

# Django
from django.urls import path

# views
from apps.users import views

urlpatterns = [
    path(
        route='users/login/',
        view=views.UserLoginAPIView.as_view(),
        name='login'
    )
]
