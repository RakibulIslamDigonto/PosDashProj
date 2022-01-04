# Generated by Django 4.0 on 2022-01-04 09:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='SellModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_date', models.DateField()),
                ('reference_no', models.CharField(max_length=50, unique=True)),
                ('Customer', models.CharField(max_length=200)),
                ('order_tax', models.CharField(choices=[('GST @5%', 'GST @5%'), ('VAT @10%', 'VAT @10%'), ('No tax', 'No tax')], max_length=50)),
                ('order_discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('attach_doc', models.FileField(blank=True, upload_to='files/')),
                ('sale_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=50)),
                ('payment_status', models.CharField(choices=[('Dew', 'Dew'), ('Pending', 'Pending'), ('Payment', 'Payment')], max_length=50)),
                ('sale_note', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('biller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biller', to='SellApp.biller')),
            ],
        ),
    ]
