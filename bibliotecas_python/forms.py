"""Docstring"""
# from django.forms import Form
# from django.forms import CharField 
# from django.forms import EmailField 
# from django.forms import PasswordInput
# from django.contrib.auth.models import User
#
# class FormNovoUsuario(Form):
#     """Docstring"""
#     nome_de_usuario = CharField() 
#     nome = CharField(required=False)
#     email = EmailField(required=False) 
#     senha = CharField(widget=PasswordInput)
#     repeticao_senha = CharField(widget=PasswordInput)

#     def save(self):
#         """Docstring"""
#         params = {
#             'username': self.cleaned_data['nome_de_usuario'], 
#             'email': self.cleaned_data['email'],
#             'password': self.cleaned_data['senha'],
#         }
#         if self.cleaned_data['nome']:
#             params['first_name'] = self.cleaned_data['nome']
#         User.objects.create_user(**params)

#     def clean_repeticao_senha(self):
#         """Docstring"""
#         senha1 = self.cleaned_data['senha']
#         senha2 = self.cleaned_data['repeticao_senha']
        
#         if senha1 != senha2:
#             raise ValidationError("As senhas devem ser iguais.")
#         return senha

from django.forms import ModelForm
from .models import Bibliotecas

class FormBiblioteca(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Bibliotecas
        fields = '__all__'