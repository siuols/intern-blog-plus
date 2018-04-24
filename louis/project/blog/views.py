from django.shortcuts import redirect, render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponseRedirect

from django.views import View

from .forms import PostForm

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

class PostCreateView(View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'blog/post_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # return redirect('post-detail', slug = post.slug)
            return redirect('blog:post-detail', slug = post.slug)
        else:
            form = PostForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

