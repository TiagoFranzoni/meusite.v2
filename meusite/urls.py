"""Docstring"""
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('meuapp/', include('meuapp.urls')),
    path('admin/', admin.site.urls),
    path('', include(('bibliotecas_python.urls', 'bibliotecas'), namespace='bibliotecas')),
]
