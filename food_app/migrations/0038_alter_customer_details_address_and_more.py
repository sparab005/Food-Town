# Generated by Django 4.2.6 on 2023-11-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0037_remove_customer_details_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_details',
            name='address',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='customer_details',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer_details',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer_details',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]
