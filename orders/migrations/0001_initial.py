# Generated by Django 2.2.7 on 2020-01-22 20:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('menu', '0002_auto_20200122_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('pizza_name', models.CharField(max_length=120)),
                ('pizza_price', models.FloatField()),
                ('creating_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('RECEIVED', 'Received'), ('PREPARING', 'Preparing'), ('OUT_FOR_DELIVERY', 'Out for delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], max_length=100)),
                ('preparation_time', models.DateTimeField()),
                ('out_for_delivery_time', models.DateTimeField()),
                ('cancellation_time', models.DateTimeField()),
                ('order_total_time', models.DurationField()),
                ('customer_name', models.CharField(max_length=120)),
                ('captain_name', models.CharField(max_length=120)),
                ('captain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Captain')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Customer')),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.PizzaPrice')),
            ],
        ),
    ]
