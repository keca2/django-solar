from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Article(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=100)
    article_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=150, default='uncategorized')
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            default='kevin',
        )
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
