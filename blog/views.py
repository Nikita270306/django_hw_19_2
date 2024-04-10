from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog_post_form.html'
    fields = ('title', 'slug', 'content', 'preview_image', 'is_published', 'views_count')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.views_count = 0
        form.instance.slug = slugify(form.instance.title)

        form.instance.is_banned = any(word in form.cleaned_data['title'].lower() or
                                      word in form.cleaned_data['content'].lower()
                                      for word in ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                                                   'free', 'scam', 'police', 'radar'])

        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'posts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog_update.html'
    fields = ('title', 'slug', 'content', 'preview_image', 'is_published', 'views_count')
    success_url = reverse_lazy('home')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog_post_confirm_delete.html'
    success_url = reverse_lazy('home')
