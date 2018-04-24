from django import forms

from .models import Post, Tag, Category

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

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'title'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title'
        ]
