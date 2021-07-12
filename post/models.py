from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100 , default='')
    body = models.CharField(max_length=500000 , default='')
    time = models.DateTimeField(datetime.now , blank=True)