from django.db import models
from django.urls import reverse

# Create your models here.

class Weight(models.Model):
    name = models.CharField(max_length=100)
    #figure out how to add units to this
    size_lbs = models.IntegerField()
    size_kgs = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weight_details', kwargs={'weight_id': self.id})