from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })

def customer_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customers/details.html', { 'customer': customer })

class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['size', 'description']

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/customers'