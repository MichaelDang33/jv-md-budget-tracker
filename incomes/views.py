from django.shortcuts import render

from .models import Income


# Create your views here.

def incomes_index(request):
   income = Income.objects.all()
   return render(request, 'incomes/index.html', {
       'income': income
   })

def home(request):
    return render(request, 'home.html')

def incomes_detail(request, income_id):
    income = Income.objects.get(id=income_id)
    return render(request, 'incomes/detail.html', {
        'income': income
    })
