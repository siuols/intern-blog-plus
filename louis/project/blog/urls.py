from django.urls import path

from . import views

from .views import (
        CommentView,
        PostCreateView,
        post_edit,
        PostDetailView,
        PostListView,
        Home,
        ProfileDetailView
        #PostEditView
    )

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post-edit'),
    path('post/<slug:slug>/comment/', CommentView.as_view(), name='comment'),
    path('profile/<username>/', ProfileDetailView.as_view(), name='profile')
    # path('post/draft/', views.post_draft, name='post-draft'),
]
