from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='incomes_index'),
    path('expenses', views.index, name='expenses_index'),
]
