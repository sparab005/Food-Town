# Generated by Django 4.2.6 on 2023-10-31 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0029_alter_cart_page_dominoid_alter_cart_page_subwayid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_page',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
