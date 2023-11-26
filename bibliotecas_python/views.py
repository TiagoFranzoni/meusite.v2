from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from bibliotecas_python.models import Bibliotecas
from django.views.generic import View
from django.shortcuts import render
from django.template import context


class BibliotecasView(ArchiveIndexView):
    """docstring"""
    model = Bibliotecas
    date_field  = 'data_de_criacao'
    template_name = 'bibliotecas/bibliotecas_archive.html'


class BibliotecasDetail(DetailView):
    """docstring"""
    model = Bibliotecas
    # template_name = 'biblioteca_detail.html'
    # context_object_name = 'biblioteca'
    # pk_url_kwarg = 'biblioteca_id'



class Home(View):
    """docstring"""
    template_name = 'bibliotecas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        # self.context['counter'] = Bibliotecas.objects.filter(nome=True).count()
        return render(request, 'bibliotecas/home.html', self.context)
