# Generated by Django 2.2.7 on 2020-01-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200123_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cancellation_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total_time',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='out_for_delivery_time',
            field=models.DateTimeField(null=True),
        ),
    ]
