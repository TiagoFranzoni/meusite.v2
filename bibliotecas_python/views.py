"""docstring"""
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from bibliotecas_python.models import Bibliotecas
from django.views.generic import View
from django.shortcuts import render
from .forms import FormBiblioteca
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import FormBiblioteca
from django.contrib import messages
from .models import Bibliotecas


class BibliotecasView(ArchiveIndexView):
    """docstring"""
    model = Bibliotecas
    date_field = 'data_de_criacao'
    template_name = 'bibliotecas/bibliotecas_archive.html'


class BibliotecasDetail(DetailView):
    """docstring"""
    model = Bibliotecas
    template_name = 'bibliotecas/bibliotecas_detail.html'
    context_object_name = 'biblioteca'
    # pk_url_kwarg = 'biblioteca_id'


class Home(View):
    """docstring"""
    template_name = 'bibliotecas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        # self.context['counter'] = Bibliotecas.objects.filter(nome=True).count()
        return render(request, 'bibliotecas/home.html', self.context)


# class CriaUsuario(View):
#     """docstring"""
#     template_name = 'templates/cria_usuario.html'
#     context = {}
    
#     def get(self, request, *args, **kwargs):
#         """docstring"""
#         self.context['form'] = FormNovoUsuario()
#         return render_to_response(self.template_name, self.context, RequestContext(request))
    
#     def post(self, request, *args, **kwargs):
#         """docstring"""
#         form = FormNovoUsuario(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             self.context['form'] = form
#             return render_to_response(self.template_name, self.context, RequestContext(request))


class AdicionaBibliotecas(View):
    """docstring"""
    template_name = 'bibliotecas/cria_biblioteca.html'
    context = {}
    
    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormBiblioteca()
        return render(request, self.template_name, self.context)
        
    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormBiblioteca(request.POST)
        if form.is_valid():
            nome_biblioteca = form.cleaned_data.get('nome')  # Substitua 'nome' pelo nome do campo correspondente
            if Bibliotecas.objects.filter(nome=nome_biblioteca).exists():
                messages.error(request, f'Uma biblioteca com o nome "{nome_biblioteca}" já existe.')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            else:
                form.save()
                return redirect('/bibliotecas/')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

