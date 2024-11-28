from django.contrib import admin
from CarBlog.models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'car', 'created_at', 'content']