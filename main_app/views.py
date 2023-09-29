from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def weight_details(request, weight_id):
    weight = Weight.objects.get(id=weight_id)
    return render(request, 'weights/details.html', { 'weight': weight })

class WeightCreate(CreateView):
    model = Weight
    fields = '__all__'

class WeightUpdate(UpdateView):
    model = Weight
    fields = ['size_lbs', 'size_kgs', 'description']

class WeightDelete(DeleteView):
    model = Weight
    success_url = '/weights'