# Generated by Django 4.0.4 on 2022-05-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('-check_out',)},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
