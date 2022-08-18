"""Faffu_Expressweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from core import views as coreviews
from core import views

from core.views import Registro, CustomLoginView, home
from django.conf import settings
from django.conf.urls.static import static
from core.forms import loginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('login/',CustomLoginView.as_view(redirect_authenticated_user=False, template_name='core/login.html',authentication_form=loginForm), name="login"),
    path('aguadesabores/', coreviews.aguadesabores, name="aguadesabores"),
    path('registro/', Registro.as_view(), name="registro"),
    path('pedidos/', coreviews.pedidos, name="pedidos"),
    path('factura/', coreviews.factura, name="factura"),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),
    path('croquetas/', coreviews.croquetas, name="croquetas"),
    path('hamburguesa/', coreviews.hamburguesa, name="hamburguesa"),
    path('pernildepollo/', coreviews.pernildepollo, name="pernildepollo"),
    path('pizza/', coreviews.pizza, name="pizza"),
    path('postre/', coreviews.postre, name="postre"),
    path('pollo/', coreviews.pollo, name="pollo"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="core/password-reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="core/password-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
