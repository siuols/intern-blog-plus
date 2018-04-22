from django.urls import path

from . import views

from .views import Index, Home

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='home')
    # path('<int:pk>/', IndexView.as_view(), name='index'),
    # path('post/<int:post_id>/', PostView.as_view(), name='post-list'),
    # path('post/comment/', views.comment_new, name='post-comment'),
    # path('post/draft/', views.post_draft, name='post-draft'),
]
