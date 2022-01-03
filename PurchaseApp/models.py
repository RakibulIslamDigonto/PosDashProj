from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from SupplierApp.models import Supplier
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Purchase(models.Model):
    RECEIVE_TYPE=(
        ('Received', 'Received'),
        ('Not Received', 'Not Received')
    )

    purchase_date= models.DateField()
    purchase_no=models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, max_length=150, on_delete=models.CASCADE, related_name='purchase_suplliar')
    discount = models.IntegerField(default=0, validators= [MinValueValidator(0), MaxValueValidator(100)], max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    receiver_type = models.CharField(choices=RECEIVE_TYPE, max_length=50, default='Received')
    order_note = models.TextField(blank=True)
    shipping = models.DecimalField(max_digits=9, decimal_places=2, blank=True)

    

