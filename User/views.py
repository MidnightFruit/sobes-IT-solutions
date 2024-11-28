from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from User.models import User
from User.forms import RegisterForm


class RegisterView(CreateView):
    """
    Контролер для регистрации пользователя.
    """
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user:login')



