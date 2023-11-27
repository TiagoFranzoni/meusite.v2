"""docstring"""
from django.urls import path
from bibliotecas_python.views import BibliotecasView, BibliotecasDetail, Home, AdicionaBibliotecas
# from bibliotecas_python.views import CriaUsuario

urlpatterns = [
    path('', Home.as_view(), name='biblioteca-home'),
    path('bibliotecas/', BibliotecasView.as_view(), name="biblioteca-view"),
    path('bibliotecas/<int:pk>/', BibliotecasDetail.as_view(), name="biblioteca-detail"),
    # path('criar_usuario/', CriaUsuario.as_view()),
    path('bibliotecas/criar/', AdicionaBibliotecas.as_view()),
]
