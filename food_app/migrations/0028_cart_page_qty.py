# Generated by Django 4.2.6 on 2023-10-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0027_remove_cart_page_resid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_page',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]