from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Expense


# Create your views here.

@login_required
def expenses_index(request):
   expense = Expense.objects.filter(user=request.user)
   return render(request, 'expenses/index.html', {
       'expense': expense
   })

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def expenses_detail(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expenses/detail.html', {
        'expense': expense
    })


class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['amount', 'date', 'category', 'description']

    success_url = '/expenses/'

    def form_valid(self, form):
        # self.request.user is the logged in user
        form.instance.user = self.request.user
        # Let the CreateView's form_valid method do its regular work
        # (saving the object & redirecting)
        return super().form_valid(form)

class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'

    success_url = '/expenses/'

class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model = Expense
    fields = '__all__'

    success_url = '/expenses/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This is how we log a user in via code
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
