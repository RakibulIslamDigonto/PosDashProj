from django.contrib import admin
from .models import Purchase

# Register your models here.
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        'purchase_date', 
        'purchase_no', 
        'supplier', 'discount', 
        'receiver_type', 'order_note', 
        'shipping'
    ]
admin.site.register(Purchase, PurchaseAdmin)