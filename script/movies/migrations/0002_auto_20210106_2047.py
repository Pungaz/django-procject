# Generated by Django 3.1.5 on 2021-01-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]