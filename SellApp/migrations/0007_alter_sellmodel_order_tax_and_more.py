# Generated by Django 4.0 on 2022-01-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellApp', '0006_alter_sellmodel_order_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='order_tax',
            field=models.CharField(choices=[('VAT @10%', 'VAT @10%'), ('GST @5%', 'GST @5%'), ('No tax', 'No tax')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='payment_status',
            field=models.CharField(choices=[('Dew', 'Dew'), ('Payment', 'Payment'), ('Pending', 'Pending')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='sale_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50),
        ),
    ]