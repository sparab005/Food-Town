# Generated by Django 4.2.6 on 2023-10-31 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0034_rename_uid_user_details_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
