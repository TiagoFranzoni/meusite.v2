from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from tarefas.models import Tarefa

# Register your models here.
class TarefaAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome', 'descricao', 'status']
    list_display = ['nome', 'descricao', 'status']
    list_editable = ['status']

site.register(Tarefa, TarefaAdmin)
