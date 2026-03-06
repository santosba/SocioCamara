from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegistrationView,LogoutView


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    #django web-token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
