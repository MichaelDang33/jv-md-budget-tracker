from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def expenses_index(request):
    return HttpResponse("Hello, world. You're at the expenses index.")

def home(request):
    return render(request, 'home.html')