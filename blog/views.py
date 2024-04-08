from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog_post_form.html'
    fields = ('title', 'slug', 'content', 'preview_image', 'is_published', 'views_count')
    success_url = reverse_lazy('/')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'posts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'preview_image', 'is_published', 'views_count')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog_post_list')
    template_name = 'blog_post_confirm_delete.html'