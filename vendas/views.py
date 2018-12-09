from django.shortcuts import render

# Create your views here.
from vendas.models import Produto


def lista_produtos(request):

    produtos = Produto.objects.all()
    return render(request, "lista_produtos.html", {'produtos' : produtos})