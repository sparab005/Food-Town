# Generated by Django 4.2.6 on 2023-11-01 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0036_customer_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_details',
            name='userid',
        ),
    ]
