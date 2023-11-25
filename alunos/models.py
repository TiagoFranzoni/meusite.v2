from django.db.models import Model
from django.db.models import CharField

# Create your models here.
class Alunos(Model):
    """Docstring"""
    codigo = CharField(max_length=20, verbose_name='codigo')
    nome = CharField(max_length=200, verbose_name='Nome')
    datanascimento = CharField(max_length=200, null=True,  blank=True, verbose_name='Data Nascimento')
    cidade = CharField(max_length=200, verbose_name='Cidade')
    logradouro = CharField(max_length=200, null=True, blank=True, verbose_name='Logradouro')
    numero = CharField(max_length=20, null=True, blank=True, verbose_name='Numero')
    bairro = CharField(max_length=200, null=True, blank=True, verbose_name='Bairro')
    cep = CharField(max_length=20, null=True, blank=True, verbose_name='CEP')

    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    uf = CharField(max_length=2, choices=UF_CHOICES, verbose_name='UF')
    
    telefone = CharField(max_length=200, null=True, blank=True, verbose_name='Telefone')
    email = CharField(max_length=200, null=True, blank=True, verbose_name='e-mail')
    cpf = CharField(max_length=200, null=True, blank=True, verbose_name='CPF')


    class Meta:
        """Docstring"""
        ordering = ['-codigo']
