from django import forms

from CarBlog.models import Car, Comment


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('owner',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude=('author', 'car',)
        
