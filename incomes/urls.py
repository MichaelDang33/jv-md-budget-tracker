from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incomes/', views.incomes_index, name='incomes_index'),
    path('incomes/<int:income_id>/', views.incomes_detail, name='incomes_detail'),
    path('incomes/create/', views.IncomeCreate.as_view(), name='incomes_create'),
    path('incomes/<int:pk>/update/', views.IncomeUpdate.as_view(), name='incomes_update'),
    path('incomes/<int:pk>/delete/', views.IncomeDelete.as_view(), name='incomes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
