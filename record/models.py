from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    

class Record(models.Model):

    user = models.ForeignKey(User, related_name='records' )
    source = models.CharField(max_length=32)
    subject = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    picture_url = models.URLField(max_length=128, null=True, blank=True)
    datetime = models.DateTimeField()
    display = models.BooleanField(default=True)
