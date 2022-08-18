from django.shortcuts import render, HttpResponse, redirect
from .forms import userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
# Create your views here.

class Registro(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'core/registro.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs): 
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect(to='/')
            return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(Registro, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
            return super(CustomLoginView, self).form_valid(form)

def password_reset(request):
    return render(request, "core/password-reset.html")



@login_required
def home(request):
    return render(request, "core/menu.html")

def pedidos(request):
    return render(request, "core/pedidos.html")

def factura(request):
    return render(request, "core/factura.html")

def aguadesabores(request):
    return render(request, "core/aguadesabores.html")

def croquetas(request):
    return render(request, "core/croquetas.html")

def hamburguesa(request):
    return render(request, "core/hamburguesa.html")

def pernildepollo(request):
    return render(request, "core/pernildepollo.html")

def pizza(request):
    return render(request, "core/pizza.html")

def pollo(request):
    return render(request, "core/pollo.html")

def postre(request):
    return render(request, "core/postre.html")


