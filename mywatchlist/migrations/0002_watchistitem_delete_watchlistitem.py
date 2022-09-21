# Generated by Django 4.1 on 2022-09-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_watched', models.CharField(default='', max_length=255)),
                ('item_title', models.CharField(default='', max_length=255)),
                ('rating', models.IntegerField(default='')),
                ('release_date', models.TextField(default='')),
                ('item_review', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='watchListItem',
        ),
    ]