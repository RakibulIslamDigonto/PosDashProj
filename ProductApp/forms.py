from django import forms
from django.db import models
from django.db.models import fields
from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        
        
