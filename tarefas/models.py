from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField 
from django.db.models import DateTimeField 
from django.db.models import TextField

# Create your models here.
class Tarefa(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    data_de_execucao = DateTimeField(verbose_name='data de execução', null=True,  blank=True)
    nome = CharField(max_length=200, verbose_name='nome')
    descricao = TextField(verbose_name='descrição', null=True, blank=True)
    status = BooleanField(default=False, verbose_name='finalizado')


    class Meta:
        """Docstring"""
        ordering = ['-data_de_execucao']
