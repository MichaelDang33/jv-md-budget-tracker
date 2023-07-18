from django.shortcuts import render
from .models import Expenses

# Create your views here.

def expenses(request):
    return render(request, 'expenses.html')

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=Expenses.objects.create(name=name,age=age,address=address)
        obj.save()
        return redirect('/expenses')
    

def retrieve(request):
    expenses=Expenses.objects.all()
    return render(request,'retrieve.html',{'expenses':expenses})