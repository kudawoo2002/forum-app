# Generated by Django 5.0.6 on 2024-06-07 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0005_remove_user_date_of_birth_user_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
