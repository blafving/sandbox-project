# Generated by Django 3.0.4 on 2020-03-31 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0002_auto_20200331_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrient',
            old_name='date_id',
            new_name='date_owner',
        ),
        migrations.RenameField(
            model_name='nutrient',
            old_name='user',
            new_name='user_owner',
        ),
    ]
