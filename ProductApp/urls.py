from django.urls import path
from django.conf.urls import include
from ProductApp.views import CategoryCreateView, CategoryList, CategoryUpdate, CategoryDetail, CategoryDelete


app_name = 'ProductApp'
urlpatterns = [
    #path('category/', CategoryCreateView.as_view(), name='category'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<slug:slug>/', CategoryUpdate.as_view(), name='category-update'),
    path('category/detail/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('category/delete/<slug:slug>/', CategoryDelete.as_view(), name='category-delete'),
    
]
