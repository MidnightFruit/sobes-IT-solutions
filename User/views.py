from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from User.models import User
from User.forms import RegisterForm, UserProfileForm


class RegisterView(CreateView):
    """
    Контролер для регистрации пользователя.
    """
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('company:login')


class ProfileView(UpdateView):
    """
    Контролер для просмотра информации пользователем про себя.
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('company:profile')

    def get_object(self, queryset=None):
        return self.request.user
