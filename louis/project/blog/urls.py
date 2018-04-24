from django.urls import path

from . import views

from .views import PostCreateView, post_edit, PostDetailView, PostEditView, PostListView, Home

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post-edit'),
    # path('post/<int:post_id>/', PostView.as_view(), name='post-list'),

    # path('post/draft/', views.post_draft, name='post-draft'),
]
