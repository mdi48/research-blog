from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('theory', 'Theory'),
        ('fiction', 'Fiction'),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists(): # handle duplicate slugs
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        return super().save(*args, **kwargs)
