from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Category
from .forms import CategoryForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class CategoryList(ListView):
    model=Category
    context_object_name = 'Categories'
    template_name= 'productApp/product_category_list.html'

class CategoryUpdate(UpdateView):

    model = Category
    fields = ('cate_name', 'parent', 'cate_image', 'code', 'is_active')
    template_name= 'productApp/product_category_update.html'
    def get_success_url(self):
        messages.success(self.request, 'Your category updated ')
        return reverse('ProductApp:category-list')


class CategoryDetail(DetailView):
    model = Category
    template_name= 'productApp/product_category_detail.html'
    context_object_name = 'category_details'


class CategoryDelete(DeleteView):
    model = Category
    template_name= 'productApp/product_category_delete.html'
    context_object_name = 'category_delete'
    def get_success_url(self):
        messages.success(self.request, 'Your category Deleted ')
        return reverse('ProductApp:category-list')



class CategoryCreateView(CreateView):
    model = Category
    fields = ('cate_name', 'parent', 'cate_image', 'code', 'is_active')
    template_name = "productApp/prod_add_category.html"
    form_classes = CategoryForm

    def get_success_url(self):
        messages.success(self.request, 'Your category added ')
        return reverse('posadminApp:home')




