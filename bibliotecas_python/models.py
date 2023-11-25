from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import URLField


# Create your models here.
class Bibliotecas(Model):
    """Docstring"""
    nome = CharField(max_length=200, verbose_name='nome da Biblioteca')
    ano = CharField(max_length=200, verbose_name='ano de Criação', null=True,  blank=True)
    descricao = TextField(verbose_name='descrição', null=True,  blank=True)
    criador = CharField(max_length=200, verbose_name='nome do criardor', null=True,  blank=True)
    mantenedor = CharField(max_length=200, verbose_name='nome do mantenedor', null=True,  blank=True)
    openSource = BooleanField(default=False, verbose_name='Open-Source', null=True,  blank=True)
    link = URLField(verbose_name='link da Biblioteca', null=True,  blank=True)

    class Meta:
        """Docstring"""
        verbose_name_plural = 'Bibliotecas'
        verbose_name = 'Biblioteca'
        ordering = ['nome']
