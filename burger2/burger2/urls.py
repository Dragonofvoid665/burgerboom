from django.contrib import admin
from django.urls import path,include
from menu.admin import orders_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('menu.urls')),
    path('admin-orders/',orders_admin_site.urls)
]
