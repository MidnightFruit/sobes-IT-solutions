from django.urls import path
from CarBlogFrontend.views import car_list
from CarBlogFrontend.apps import CarblogfrontendConfig


app_name = CarblogfrontendConfig.name

urlpatterns = [
    path("main/", car_list, name="main"),
]
