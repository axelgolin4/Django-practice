from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.urls')),
    path('products/', include('apps.products.urls')),
]
