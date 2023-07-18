from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incomes/', views.incomes_index, name='incomes_index'),
    path('incomes/<int:income_id>/', views.incomes_detail, name='incomes_detail'),
]
