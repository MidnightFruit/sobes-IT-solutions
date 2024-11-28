from django.urls import path
from CarBlogFrontend.views import car_list, car_create
from CarBlogFrontend.apps import CarblogfrontendConfig


app_name = CarblogfrontendConfig.name

urlpatterns = [
    path("main/", car_list, name="main"),
    path("create_car/", car_create, name="create_car"),
    #path("update_car/<int:pk>", car_update, name="update_car"),
    #path("delete_car/<int:pk>", car_delete, name="delete_car"),
]
