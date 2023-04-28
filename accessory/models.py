from django.db import models

class Accessory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='Accessory_images' ,blank=False, null=True)
    count = models.IntegerField(default=1)
    price = models.CharField(null=True, blank=False, max_length=20)
    def __str__(self):
        return self.name