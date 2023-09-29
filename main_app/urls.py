from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('weights/', views.weights_index, name='weights_index'),
    path('weights/<int:weight_id>/', views.weight_details, name='weight_details'),
    path('weights/create/', views.WeightCreate.as_view(), name='weight_create'),
    path('weights/<int:pk>/update/', views.WeightUpdate.as_view(), name='weight_update'),
    path('weights/<int:pk>/delete/', views.WeightDelete.as_view(), name='weight_delete'),
]