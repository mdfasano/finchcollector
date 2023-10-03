from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Customer, Workout, Weight
from .forms import WorkoutForm
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
    workout_form = WorkoutForm()
    id_list = customer.weights.all().values_list('id')
    weights_c_doesnt_have = Weight.objects.exclude(id__in=id_list)
    return render(request, 'customers/details.html', {
        'customer': customer,
        'workout_form': workout_form,
        'weights': weights_c_doesnt_have,
        })

def assoc_weight(request, customer_id, weight_id):
    Customer.objects.get(id=customer_id).weights.add(weight_id)
    return redirect('customer_details', customer_id=customer_id)

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'size', 'description']

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['size', 'description']

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/customers'

def add_workout(request, customer_id):
    # return redirect('/about/')
    form = WorkoutForm(request.POST)
    if form.is_valid():
        new_workout = form.save(commit=False)
        new_workout.customer_id = customer_id
        new_workout.save()
    return redirect('customer_details', customer_id=customer_id)

class WorkoutDelete(DeleteView):
    model = Workout
    
    def get_success_url(self):
        customer_id = self.object.customer_id
        return reverse(
            'customer_details', 
            kwargs = {'customer_id': customer_id}
        )
    
class WeightList(ListView):
    model = Weight

class WeightDetail(DetailView):
    model = Weight

class WeightDelete(DeleteView):
    model = Weight
    success_url = '/about/'

class WeightCreate(CreateView):
    model = Weight
    fields = '__all__'

class WeightUpdate(UpdateView):
    model = Weight
    fields = ['name', 'size_lbs']