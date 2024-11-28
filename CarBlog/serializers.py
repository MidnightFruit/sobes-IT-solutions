from rest_framework import serializers

from CarBlog.models import Car, Comment


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        extra_kwargs = {
            'owner': {'required': False} 
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            'car': {'required': False},
            'author': {'required': False},
        }