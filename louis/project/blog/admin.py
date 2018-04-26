from django.contrib import admin

from .models import Category, Comment, Tag, Post

# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post)
