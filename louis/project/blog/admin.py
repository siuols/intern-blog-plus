from django.contrib import admin

from .models import Category, Comment, Tag, Post, Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Profile)
