# Generated by Django 3.0.8 on 2020-08-08 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('SELLER', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopownerprofile',
            name='TIN_number',
        ),
        migrations.RemoveField(
            model_name='shopregistration',
            name='shop_type',
        ),
    ]