# Generated by Django 3.0.8 on 2020-08-30 10:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('SELLER', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='shopownerbankdetails',
            table='tbl_shop_owner_bank_details',
        ),
        migrations.AlterModelTable(
            name='shopownerprofile',
            table='tbl_shop_owner_profile',
        ),
        migrations.AlterModelTable(
            name='shopregistration',
            table='tbl_registered_shops',
        ),
    ]
