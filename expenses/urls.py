from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses', views.index, name='expenses_index'),
]