# Generated by Django 4.0 on 2021-12-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cate_name',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=60, unique=True),
        ),
    ]
