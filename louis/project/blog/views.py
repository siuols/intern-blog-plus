from django.shortcuts import render

from django.views import View

from .models import Category, Tag, Post

# Create your views here.

class Home(View):
    def get(self, request, *arg, **kwargs):
        post = Post.objects.all()
        context = {
            'post': post,
        }
        return render(request, 'blog/home.html', context)

class Index(View):
    def get(self, request,*arg, **kwargs):
        post = Post.objects.all()
        context = {
            'post': post,
        }
        return render(request,'blog/index.html', context)
