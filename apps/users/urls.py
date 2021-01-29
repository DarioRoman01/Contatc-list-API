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
    ),

    path(
        route='users/verify',
        view=views.UserVerificationAPIView.as_view(),
        name='verify'
    ),

    path(
        route='users/signup/',
        view=views.UserSignupAPIView.as_view(),
        name='signup'
    )
]
