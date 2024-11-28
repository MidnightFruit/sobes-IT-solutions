from django.shortcuts import render
from django.urls import reverse


def car_list(request):
    response = request.get(reverse('cars:cars-list'))
    return render(request, 'CarBlog/index.html', {'car':response.json()})