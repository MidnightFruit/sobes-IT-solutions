from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView, LogoutView

from User.apps import UserConfig
from User.views import RegisterView


app_name = UserConfig.name

urlpatterns = [
    path("register_user/", RegisterView.as_view(), name="register_user"),
    path('login/', LoginView.as_view(template_name='User/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("obtain/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
