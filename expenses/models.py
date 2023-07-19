from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    # add user_id FK column
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('expenses_detail', kwargs={'expenses_id': self.id})

    