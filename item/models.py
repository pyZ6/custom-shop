from django.db import models
from django.contrib.auth.models import User
import uuid
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
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
    
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
    #python manage.py shell
    #item.objects.count() return the number of items
    #item.objects.filter(category__name="Shoes") return only items with shoes category
    #from django.db.models import Avg, Max