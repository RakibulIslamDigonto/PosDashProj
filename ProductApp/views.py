from django.db.models import fields
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Category
# Create your views here.

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = "productApp/prod_add_category.html"



