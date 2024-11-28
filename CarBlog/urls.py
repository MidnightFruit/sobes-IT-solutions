from django.urls import path
from rest_framework.routers import DefaultRouter

from CarBlog.apps import CarblogConfig
from CarBlog.views import CarViewSet, CommentView


app_name = CarblogConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path("cars/<int:pk>/comments/", CommentView.as_view(), name="comments"),
] + router.urls
