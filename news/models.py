from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    
    
    def __unicode__(self):
        return self.title;
    
    class Meta(object):
        verbose_name_plural = "News"