# Generated by Django 5.1.1 on 2024-09-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Done', 'Done')], max_length=15),
        ),
    ]
