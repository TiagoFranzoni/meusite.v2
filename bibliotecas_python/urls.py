"""docstring"""
from django.urls import path
from bibliotecas_python.views import BibliotecasView, BibliotecasDetail, Home, AdicionaBibliotecas, ExcluiBibliotecas, EditaBibliotecas
from bibliotecas_python.views import Login, CriaUsuario

urlpatterns = [
    path('', Home.as_view(), name='biblioteca-home'),
    
    path('bibliotecas/', BibliotecasView.as_view(), name="biblioteca-view"),
    path('bibliotecas/<int:pk>/', BibliotecasDetail.as_view(), name='biblioteca-detail'),
    path('bibliotecas/criar/', AdicionaBibliotecas.as_view()),
    path('bibliotecas/<int:pk>/deletar/', ExcluiBibliotecas.as_view(), name='biblioteca-deletar'),
    path('bibliotecas/<int:pk>/editar/', EditaBibliotecas.as_view(), name='biblioteca-editar'),
    
    path('criar_usuario/', CriaUsuario.as_view()),
    path('login/', Login.as_view()),
    ]
