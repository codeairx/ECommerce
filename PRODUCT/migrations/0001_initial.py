# Generated by Django 3.0.8 on 2020-08-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SELLER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MasterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=200)),
                ('parent_category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.MasterCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_stoke', models.IntegerField()),
                ('product_MRP', models.IntegerField()),
                ('product_selling_price', models.IntegerField()),
                ('product_master_category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.MasterCategory')),
                ('product_shop',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SELLER.ShopRegistration')),
                ('product_sub_category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.SubCategory')),
                ('seller', models.ManyToManyField(related_name='seller_product_table', to='SELLER.ShopRegistration')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novel_title', models.CharField(max_length=255)),
                ('novel_author', models.CharField(max_length=255)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.Product')),
            ],
        ),
        migrations.CreateModel(
            name='MobileSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type', models.CharField(
                    choices=[('Android', 'Android'), ('iPhone', 'iPhone'), ('Feature Phone', 'Feature Phone'),
                             ('Tablet', 'Tablet')], max_length=100)),
                ('brand', models.CharField(max_length=200)),
                ('phone_name', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200, null=True)),
                ('launch_date', models.DateField(null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.Product')),
            ],
        ),
        migrations.CreateModel(
            name='LaptopVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=255)),
                ('RAM', models.IntegerField()),
                ('storage', models.CharField(max_length=100)),
                ('price_by_variant', models.BigIntegerField()),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.Laptop')),
            ],
        ),
        migrations.AddField(
            model_name='laptop',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.Product'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=255)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.Product')),
            ],
        ),
    ]
