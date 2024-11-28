import requests
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

API_BASE_URL = 'http://localhost:8000/'


def car_list(request):
    response = requests.get(f"{API_BASE_URL}{reverse_lazy('cars:cars-list')}")
    return render(request, 'CarBlog/CarBlog.html', {'car':response.json()})


def car_create(request):
    if request.method == 'POST':
        data = {
            'make': request.POST['make'],
            'model': request.POST['model'],
            'year': request.POST['year'],
            'description': request.POST['description'],
        }
        token, created  = Token.objects.get_or_create(user=request.user)

        header = {
            'Authorization': f'Token {token.key}',
        }
        session = requests.Session()
        session.auth()
        response = requests.post(f"{API_BASE_URL}/api/cars/", data=data,headers=header, auth=)
        if response.status_code == 201:
            return redirect('car_list')
    return render(request, 'CarBlog/car_form.html')