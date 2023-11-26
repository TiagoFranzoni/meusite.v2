# from django.contrib import admin 
from django.urls import path
from bibliotecas_python.views import BibliotecasView, BibliotecasDetail, Home

urlpatterns = [
    path('', Home.as_view(), name='biblioteca-home'),
    path('bibliotecas/', BibliotecasView.as_view(), name="biblioteca-view"),
    path('bibliotecas/<int:pk>/', BibliotecasDetail.as_view(), name="biblioteca-detail"),
]
