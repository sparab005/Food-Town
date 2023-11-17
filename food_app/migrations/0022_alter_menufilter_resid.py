# Generated by Django 4.2.6 on 2023-10-29 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0021_menufilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menufilter',
            name='resid',
            field=models.ForeignKey(choices=[(1, 'burger'), (2, 'pizza'), (3, 'Chinease'), (4, 'Biryani'), (5, 'Cakes'), (6, 'South Indian'), (7, 'Pure Veg'), (8, 'Dessarts')], db_column='resid', on_delete=django.db.models.deletion.CASCADE, to='food_app.toprestaurant'),
        ),
    ]