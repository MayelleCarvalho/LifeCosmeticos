"""life_cosmeticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from vendas import views
import vendas
from perfis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vendas.views.lista_produtos, name='index'),
    path('add_produto/', vendas.views.add_produtos, name='add_produtos'),
    path('add_perfil/', views.add_perfil, name='add_perfil'),
    path('produtos/', vendas.views.lista_produtos, name= 'lista_produtos'),
    path('produto/<int:produto_id>/', vendas.views.detalhar_produto, name= 'detalhar_produto'),
    path('produto/<int:produto_id>/editar', vendas.views.editar_produto, name= 'editar_produto'),
]
