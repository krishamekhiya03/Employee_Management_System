# Generated by Django 5.0.7 on 2024-08-06 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dob',
            new_name='Date_Of_Birth',
        ),
    ]
