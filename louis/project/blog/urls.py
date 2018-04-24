from django.urls import path

from . import views

from .views import PostListView, PostDetailView, Home

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    # path('<int:pk>/', PostDetailView.as_view(), name='index'),
    # path('post/<int:post_id>/', PostView.as_view(), name='post-list'),
    # path('post/comment/', views.comment_new, name='post-comment'),
    # path('post/draft/', views.post_draft, name='post-draft'),
]
