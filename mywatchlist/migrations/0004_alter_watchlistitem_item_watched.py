# Generated by Django 4.1 on 2022-11-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_rename_watchistitem_watchlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='item_watched',
            field=models.BooleanField(),
        ),
    ]