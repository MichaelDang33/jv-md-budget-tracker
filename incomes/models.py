from django.db import models

# Create your models here.

class Income(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()
    #owner = models.ForeignKey(to=User)
    source = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.source} ({self.id})'

