from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    """
        News(title, body, image = NULL, creator, creation_date, published_date)
    """
    title = models.CharField(max_length = 50)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images', null=True, blank=True)
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    
    
    def __unicode__(self):
        return self.title;
    
    
    class Meta(object):
        verbose_name_plural = "News"
        ordering = ["-published_date"]
        
