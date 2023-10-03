from django.contrib import admin
from .models import Customer, Workout, Weight
# Register your models here.

admin.site.register(Customer)
admin.site.register(Workout)
admin.site.register(Weight)