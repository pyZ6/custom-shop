from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    def __str__(self):
        return self.title
class Song(models.Model):
    name = models.CharField(max_length=30)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
