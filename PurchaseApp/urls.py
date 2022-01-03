from django.urls import path
from django.conf.urls import include
from .views import PurchaseCreateView


app_name = 'PurchaseApp'
urlpatterns = [
    path('', PurchaseCreateView.as_view(), name='purchase-add'),

]