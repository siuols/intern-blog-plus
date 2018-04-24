from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import View

from .models import Category, Tag, Post

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        context = {
            'post': post,
        }
        return render(request, 'blog/home.html', context)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        post_list = Post.objects.filter(status='published')
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
        context = {
            'post': post,
        }
        return render(request,'blog/post_list.html', context)

class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post_detail = get_object_or_404(Post, slug = slug)
        context = {
            'post': post_detail
        }
        return render(request, 'blog/post_detail.html', context)
