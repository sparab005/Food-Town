# Generated by Django 4.2.6 on 2023-11-08 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0059_alter_orderconfirmed_oid_alter_orderconfirmed_pid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconfirmed',
            name='oid',
            field=models.ForeignKey(db_column='oid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.orderp', to_field='order_id'),
        ),
        migrations.AlterField(
            model_name='orderconfirmed',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.CASCADE, to='food_app.food'),
        ),
        migrations.AlterField(
            model_name='orderconfirmed',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
