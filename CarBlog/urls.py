from django.urls import path

from CarBlog.apps import CarblogConfig
from CarBlog.views import CarCreateAPIView, CarRetrieveAPIView, CarUpdateAPIView, CarListView, CommentCreateAPIView, \
    CommentListAPIView, CarDestroyAPIView


app_name = CarblogConfig.name


urlpatterns = [
    path("cars/", CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>", CarRetrieveAPIView.as_view(), name="car_retriveve"),
    path("cars/", CarCreateAPIView.as_view(), name="car_create"),
    path("cars/<int:pk>", CarUpdateAPIView.as_view(), name="car_update"),
    path("cars/<int:pk>", CarDestroyAPIView.as_view(), name="car_destroy"),
    path("cars/<int:car_id>/comments/", CommentListAPIView.as_view(), name="comment_list"),
    path("cars/<int:car_id>/comments/", CommentCreateAPIView.as_view(), name="comment_list"),
]
