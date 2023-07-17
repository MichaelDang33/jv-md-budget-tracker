from django.urls import path
from . import views

# from django.urls import re_path as url


urlpatterns = [
    path('', views.expenses, name='expenses'),
    path('create', views.create, name='create'),
    path('retrieve',views.retrieve,name="retrieve"),

]