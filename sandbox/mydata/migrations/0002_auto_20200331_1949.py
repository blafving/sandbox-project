# Generated by Django 3.0.4 on 2020-03-31 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrient',
            old_name='date',
            new_name='date_id',
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mydata.User'),
        ),
    ]
