from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from alunos.models import Alunos

# Register your models here.
class AlunosAdmin(ModelAdmin):
    """Docstring"""
    fields = ['codigo', 'nome', 'datanascimento', 'cidade', 'logradouro', 'numero', 'bairro', 'cep', 'uf', 'telefone', 'email', 'cpf']
    list_display = ['codigo', 'nome', 'datanascimento', 'cidade', 'logradouro', 'numero', 'bairro', 'cep', 'uf', 'telefone', 'email', 'cpf']

site.register(Alunos, AlunosAdmin)