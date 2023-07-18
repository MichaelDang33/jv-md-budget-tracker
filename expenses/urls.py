from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.expenses_index, name='expenses_index'),
    path('expenses/<int:income_id>/', views.expenses_detail, name='expenses_detail'),
]