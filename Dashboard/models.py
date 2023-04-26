from django.db import models
    
class Dashboard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name