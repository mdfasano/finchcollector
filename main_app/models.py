from django.db import models
from django.urls import reverse

# Create your models here.

class Weight(models.Model):
    name = models.CharField(max_length=50)
    size_lbs = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weight_detail', kwargs={'pk': self.id})

class Customer(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('customer_details', kwargs={'customer_id': self.id})
    
    def exercised_today(self):
        return self.workout_set.count() >= 2
    

class Workout(models.Model):
    name = models.CharField(max_length=25)
    difficulty = models.CharField(max_length=10)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_customer_url(self):
        return reverse('customer_details', kwargs={'customer_id': self.customer})