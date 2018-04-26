from django.shortcuts import redirect, render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect

from django.views import View

from .forms import (
            CommentForm,
            CategoryForm,
            TagForm,
            RegistrationForm,
            PostForm,
            ProfileForm
        )

from .models import Category, Tag, Post, Profile

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
            return redirect('blog:post-detail', slug = post.slug)
        else:
            form = PostForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def  post_edit(request, slug):
    post_user = Post.objects.filter(user=request.user)
    post = get_object_or_404(post_user, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post-detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

class CommentView(View):
    form_class = CommentForm
    initial = {'key': 'value'}
    template_name = 'blog/comment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('blog:post-detail', slug = post.slug)
        else:
            form = CommentForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

class RegisterFormView(View):
    form_class = RegistrationForm
    second_form_class = ProfileForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class(initial=self.initial)
        profile_form = self.second_form_class(initial=self.initial)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        profile_form = self.second_form_class(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile_form = profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            return redirect('blog:post-list')
        else:
            form = RegistrationForm()
            profile_form = ProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

class IndexView(View):
    def get(self, request, pk, *args, **kwargs):
      index = get_object_or_404(Index, pk=pk)
      post_list = index.post_set.filter(status='published')

class ProfileDetailView(View):
    def get(self, request, username, *args, **kwargs):
        profile_detail = get_object_or_404(User, username__iexact=username)
        post_list = profile_detail.post_set.filter(user=self.request.user, status='published')
        paginator = Paginator(post_list, 10)
        page = request.GET.get('page')
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
        context = {
            'profile_detail': profile_detail,
            'post': post,
        }
        return render(request, 'blog/profile_detail.html', context)
