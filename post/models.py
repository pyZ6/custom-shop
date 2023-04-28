from django.db import models

class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    def __unicode__(self):
        return unicode(self.post_heading)