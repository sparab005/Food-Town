# Generated by Django 4.2.6 on 2023-11-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0050_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='foodname',
            field=models.CharField(max_length=150, verbose_name='FoodName '),
        ),
    ]
