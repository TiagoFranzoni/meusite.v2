"""Docstring"""
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('meuapp/', include('meuapp.urls')),
    path('admin/', admin.site.urls),
    path('', include(('bibliotecas_python.urls', 'bibliotecas'), namespace='bibliotecas')),
    path('logout/', auth_views.LogoutView.as_view(next_page='bibliotecas:biblioteca-home'), name='logout'),
]
