from django.urls import path
from django.conf.urls import include
from ProductApp.views import CategoryCreateView


app_name = 'ProductApp'
urlpatterns = [
    path('category/', CategoryCreateView.as_view(), name='category')
]
