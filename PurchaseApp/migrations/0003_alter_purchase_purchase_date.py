# Generated by Django 4.0 on 2022-01-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0002_alter_purchase_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateTimeField(),
        ),
    ]
