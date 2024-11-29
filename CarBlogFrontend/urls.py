from django.urls import path
from CarBlogFrontend.views import CarListView, CarCreateView, CarTemplateView, CarUpdateView, CarDeleteView
from CarBlogFrontend.apps import CarblogfrontendConfig


app_name = CarblogfrontendConfig.name

urlpatterns = [
    path("main/", CarListView.as_view(), name="main"),
    path("create_car/", CarCreateView.as_view(), name="create_car"),
    path("car/<int:pk>/", CarTemplateView.as_view(), name="car"),
    path("update_car/<int:pk>", CarUpdateView.as_view(), name="update_car"),
    path("delete_car/<int:pk>", CarDeleteView.as_view(), name="delete_car"), 
]
