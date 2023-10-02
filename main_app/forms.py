from django.forms import ModelForm
from .models import Workout

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'difficulty', 'description']