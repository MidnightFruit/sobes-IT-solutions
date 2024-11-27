from django.shortcuts import render

from CarBlog.serializers import CarSerializer, CommentSerializer

from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404

from CarBlog.models import Car, Comment

from rest_framework.permissions import IsAuthenticated, AllowAny


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class =CarSerializer


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        car_pk = self.kwargs.get('car_id')
        car_item = get_object_or_404(Car, pk = car_pk)
        serializer.save(author=self.request.user, car=car_item)

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        car_pk = self.kwargs.get('car_id')
        car_item = get_object_or_404(Car, pk = car_pk)
        data = Comment.objects.get(car=car_item)
        return data
    