# Generated by Django 2.2.7 on 2020-01-24 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200123_1928'),
        ('menu', '0003_pizzaprice_preparation_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PizzaPrice',
            new_name='PizzaType',
        ),
    ]
