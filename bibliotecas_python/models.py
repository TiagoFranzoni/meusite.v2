from django.db.models import Model, BooleanField, CharField, TextField, URLField, IntegerField, DateTimeField

# Create your models here.
class Bibliotecas(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome da Biblioteca')
    ano = IntegerField(verbose_name='ano de Criação', null=True,  blank=True)
    descricao = TextField(verbose_name='descrição', null=True,  blank=True)
    criador = CharField(max_length=200, verbose_name='nome do criardor', null=True,  blank=True)
    mantenedor = CharField(max_length=200, verbose_name='nome do mantenedor', null=True,  blank=True)
    openSource = BooleanField(default=False, verbose_name='Open-Source', null=True,  blank=True)
    link = URLField(verbose_name='link da Biblioteca', null=True,  blank=True)

    # def save(self, *args, **kwargs):
    #     if self.ano:
    #         self.ano_date = DateField(year=self.ano, month=1, day=1)
    #     super().save(*args, **kwargs)

    class Meta:
        """Docstring"""
        verbose_name_plural = 'Bibliotecas'
        verbose_name = 'Biblioteca'
        ordering = ['nome']
