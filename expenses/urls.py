from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.expenses_index, name='expenses_index'),
]