# Generated by Django 4.1 on 2022-09-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_rename_item_date_task_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
