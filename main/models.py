from django.db import models

class Collections(models.Model):
    image = models.ImageField(upload_to='media/collections')
    name = models.CharField(max_length = 30, default = 'some titled picture')
    category = models.CharField(max_length = 20, default = 'Image')
    items_in_collection = models.CharField(max_length = 25, default = '1/1')

class Market(models.Model):
    image = models.ImageField(upload_to='media/market')
    name = models.CharField(max_length = 30, default = 'some titled picture')
    author_name = models.CharField(max_length = 20, default = 'Owner')
    author_link = models.CharField(max_length = 40, default = '@author_link')
    ends_in = models.DateTimeField()
    current_bid = models.CharField(max_length = 25)
    current_price = models.CharField(max_length = 25)

# Create your models here.
