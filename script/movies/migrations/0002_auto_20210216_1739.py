# Generated by Django 3.1.5 on 2021-02-16 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{4,4}$')]),
        ),
    ]