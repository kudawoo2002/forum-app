# Generated by Django 5.0.6 on 2024-05-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
