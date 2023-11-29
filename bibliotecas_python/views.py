"""docstring"""
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from bibliotecas_python.models import Bibliotecas
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import FormBiblioteca, FormLogin, FormNovoUsuario
from django.template import RequestContext
from django.contrib import messages
from django.urls import reverse
from .models import Bibliotecas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(View):
    """docstring"""
    template_name = 'bibliotecas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        # self.context['counter'] = Bibliotecas.objects.filter(nome=True).count()
        return render(request, 'bibliotecas/home.html', self.context)


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
            nome_biblioteca = form.cleaned_data.get('nome')
            if Bibliotecas.objects.filter(nome=nome_biblioteca).exists():
                messages.error(request, f'Uma biblioteca com o nome "{nome_biblioteca}" já existe.')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/bibliotecas/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class EditaBibliotecas(UpdateView):
    """docstring"""
    model = Bibliotecas
    form_class = FormBiblioteca
    template_name = 'bibliotecas/edita_biblioteca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biblioteca'] = self.object
        return context

    def get_success_url(self):
        return '/bibliotecas/'


class ExcluiBibliotecas(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormBiblioteca()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        biblioteca = Bibliotecas.objects.get(pk=kwargs['pk'])
        biblioteca.delete()
        return redirect('/bibliotecas/')


class Login(View):
    """docstring"""
    template_name = 'login_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormLogin()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nome_de_usuario')
            password = form.cleaned_data.get('senha')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            messages.warning(request, 'Nome de usuário ou senha inválidos')
        self.context['form'] = form
        return render(request, self.template_name, self.context)



    def clean(self):
        """docstring"""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class CriaUsuario(View):
    """docstring"""
    template_name = 'criar_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormNovoUsuario()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nome_de_usuario')
            password = form.cleaned_data.get('senha')
            first_name = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            # user = User.objects.create_user(username=username, password=password)
            user = User.objects.create_user(username=username, first_name=first_name, email=email)
            user.set_password(password)
            user.save()
            # login(request, user)
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/login/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)