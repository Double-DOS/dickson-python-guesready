# Generated by Django 4.0.4 on 2022-05-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(unique=True),
        ),
    ]
