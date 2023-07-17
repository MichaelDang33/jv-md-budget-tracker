from django.shortcuts import render
from django.http import HttpResponse
from .models import income

# Create your views here.

def incomes_index(request):
    incomes = income.objects.all()
    return render(request, 'incomes.html', {
         'incomes': income
    })

def home(request):
    incomes = income.objects.all()
    return render(request, 'home.html', {
        'incomes': income
    })