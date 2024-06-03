from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    Category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_pic/')

    class Meta:
        verbose_name = "Category"
        verbose_name_plurak:"Categories"

    def __str__(self):
        return self.Category_name


class Forum(models.Model):
    Category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='Forum_pic/', blank=True, default='apod.jpg')
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    # published = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title