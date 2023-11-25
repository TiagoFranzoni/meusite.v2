from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from bibliotecas_python.models import Bibliotecas

# Register your models here.
class BibliotecaAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome','ano', 'descricao', 'criador', 'mantenedor', 'openSource', 'link']
    list_display = ['nome','ano', 'descricao', 'criador', 'mantenedor', 'openSource', 'link']
    list_editable = ['openSource']

site.register(Bibliotecas, BibliotecaAdmin)