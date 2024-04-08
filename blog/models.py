from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
