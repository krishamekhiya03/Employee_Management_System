# Generated by Django 5.0.7 on 2024-08-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_alter_employee_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
