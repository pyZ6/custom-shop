from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    instruments = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    related_date = models.DateField()
    monthly_income = models.BigIntegerField(default=1000, blank=True, help_text="arbitrariness")
    published = models.BooleanField(default=True)
    published_time = models.DateTimeField(auto_now=True)
    Email = models.EmailField(blank=False, null=True, help_text="Enter the Musician Email")
    image = models.ImageField(upload_to='Album_images',blank=True, null=True)
    def __str__(self):
        return self.name