from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'banner_photo',
            'tags',
            'category',
            'body',
            'status'
        ]
