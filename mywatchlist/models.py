from django.db import models

# Create your models here.
class watchlistItem(models.Model):
    item_watched = models.CharField(max_length=255, default='')
    item_title = models.CharField(max_length=255, default='')
    rating = models.IntegerField(default='')
    release_date = models.TextField(default='')
    item_review = models.TextField(default='')