from django import forms
from .models import Purchase


class PurchaseFrom(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'order_note': forms.Textarea(attrs={'rows': '3'}),

        }


