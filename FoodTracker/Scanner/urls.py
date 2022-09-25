from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-items/', views.addItems, name='addItems'),
    path('remove-items/', views.removeItems, name='removeItems'),
]