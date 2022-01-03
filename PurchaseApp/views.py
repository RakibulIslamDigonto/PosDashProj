from django.shortcuts import render
from .models import Purchase
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.urls import reverse
from .forms import PurchaseFrom
from ProductApp.models import Product


#Create your views here.
class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "purchaseApp/purchase_add.html"
    form_class = PurchaseFrom

    def get_success_url(self):
        messages.success(self.request, 'Your purchase added ')
        return reverse('posadminApp:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Pruducts"] = Product.objects.all()
        return context
    

