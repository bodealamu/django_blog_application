from django.db import models
from datetime import datetime
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    """ Model representation for blog post categpries."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True,
                            verbose_name='Category name')

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Model representation for a Blog Post Object"""
    id = models.AutoField(primary_key =True)
    title = models.CharField(unique=True, max_length=100, verbose_name='Ttle of the Blog Post')
    picture_location = models.ImageField(upload_to='images/', max_length=120)
    body = models.TextField(verbose_name='Blog content')
    created_at = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=False)
    category_name = models.ForeignKey(to=Category, to_field='name',on_delete=models.CASCADE)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    blog_slug = models.SlugField(default='abc', unique=True)

    def save(self, *args, **kwargs):
        self.blog_slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_slug


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='Your full name')
    email = models.EmailField(max_length=60, verbose_name='Your email address')
    body = models.TextField(verbose_name='Add your comment here')
    created_on = models.DateTimeField(default=datetime.now())
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name



