# Generated by Django 4.2.3 on 2023-07-17 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0002_rename_income_incomes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Incomes',
            new_name='Income',
        ),
    ]