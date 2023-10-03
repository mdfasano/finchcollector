from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('customers/', views.customers_index, name='customers_index'),
    path('customers/<int:customer_id>/', views.customer_details, name='customer_details'),
    path('customers/create/', views.CustomerCreate.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer_delete'),
    path('customers/<int:customer_id>/add_workout/', views.add_workout, name='add_workout'),
    path('workout/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout_delete')
]