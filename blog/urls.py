from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_post_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
]
