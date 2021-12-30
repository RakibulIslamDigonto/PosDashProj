
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posadminApp.urls')),
    path('product/', include('ProductApp.urls', namespace='ProductApp')),
    path('supplier/', include('SupplierApp.urls', namespace='SupplierApp'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    