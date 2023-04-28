from django.contrib import admin

from .models import Category, Item, Musician, Album,Cart, CartItem

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Cart)
admin.site.register(CartItem)
