from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

from CarBlog.serializers import CarSerializer, CommentSerializer
from CarBlog.models import Car, Comment
from User.permissions import IsOwner



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated,]
        elif self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [AllowAny]

        return [permission() for permission in self.permission_classes]

class CommentView(GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        car_pk = self.kwargs.get('pk')
        car_item = get_object_or_404(Car, pk=car_pk)
        data = Comment.objects.filter(car=car_item)
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_pk = self.kwargs.get('pk')
        car_item = get_object_or_404(Car, pk = car_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            serializer.save(car=car_item, author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class CommentCreateAPIView(CreateAPIView):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer
#    permission_classes = [IsAuthenticated]
#
#    def perform_create(self, serializer):
#        car_pk = self.kwargs.get('car_id')
#        car_item = get_object_or_404(Car, pk = car_pk)
#        serializer.save(author=self.request.user, car=car_item)
#
#class CommentListAPIView(ListAPIView):
#    queryset = Comment.objects.all()
#    serializer_class = CommentSerializer
#
#    def get_queryset(self):
#        car_pk = self.kwargs.get('car_id')
#        car_item = get_object_or_404(Car, pk = car_pk)
#        data = Comment.objects.get(car=car_item)
#        return data
    