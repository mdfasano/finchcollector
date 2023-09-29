from django.shortcuts import render
from .models import Weight
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def weights_index(request):
    weights = Weight.objects.all()
    return render(request, 'weights/index.html', {
        'weights': weights
    })

def weights_detail(request, weight_id):
    weight = Weight.objects.get(id=weight_id)
    return render(request, 'weights/details.html', { 'weight': weight })