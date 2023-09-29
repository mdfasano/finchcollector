from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('weights/', views.weights_index, name='index'),
    path('weights/<int:weight_id>/', views.weights_detail, name='details'),
]