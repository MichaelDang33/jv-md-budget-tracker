from django.urls import path
from . import views

# from django.urls import re_path as url


urlpatterns = [

    path('', views.home, name='home'),
    path('expenses/', views.expenses_index, name='expenses_index'),
    path('expenses/<int:income_id>/', views.expenses_detail, name='expenses_detail'),

    path('', views.expenses, name='expenses'),
    path('create', views.create, name='create'),
    path('retrieve',views.retrieve,name="retrieve"),


]