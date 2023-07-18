from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense

# Create your views here.

def expenses_index(request):
   expense = Expense.objects.all()
   return render(request, 'expenses/index.html', {
       'expense': expense
   })

def home(request):
    return render(request, 'home.html')

def expenses_detail(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expenses/detail.html', {
        'expense': expense
    })