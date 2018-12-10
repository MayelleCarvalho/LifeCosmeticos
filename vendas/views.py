import datetime

from django.shortcuts import render, redirect

# Create your views here.
from vendas.forms import ProdutoForm
from vendas.models import Produto, Categoria, Venda, ItemVenda
from perfis.views import *


def add_produtos(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'add_produtos.html',
                          {'form': form})
    else:
        form = ProdutoForm()
        return render(request, 'add_produtos.html',
                      {'form': form})


def lista_produtos(request):

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "lista_produtos.html", {'produtos' : produtos, 'categorias': categorias})


def lista_compras(request):

    vendas = Venda.objects.filter(cliente=get_perfil_logado())
    return render(request, "lista_compras.html", {'vendas' : vendas})


def detalhar_produto(request, produto_id):

    produto = Produto.objects.get(id=produto_id)
    return render(request, 'detalhar_produto.html',
                  {'produto': produto})


def filtrar_produtos(request, categoria_produto):

    produtos = Produto.objects.filter(categoria=categoria_produto)
    categorias = Categoria.objects.all()
    return render(request, "lista_produtos.html", {'produtos': produtos, 'categorias': categorias})


def editar_produto(request, produto_id):

    produto = Produto.objects.get(id=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ProdutoForm(instance=produto)

        return render(request, "editar_produto.html",
                      {'form': form})


def adicionar_item_venda(request, produto_id, venda_id):

    produto = Produto.objects.get(id=produto_id)
    venda = Venda.objects.get(id=venda_id)
    item = ItemVenda.objects.create(venda=venda, item=produto, valor_total_item=produto.valor_unit)
    venda.valor_total += item.valor_total_item
    venda.save()

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "lista_produtos.html",
                  {'produtos': produtos,
                   'categorias': categorias,
                   'venda': venda})


def realizar_venda(request, produto_id):

    produto = Produto.objects.get(id=produto_id)

    venda = Venda.objects.create(cliente=get_perfil_logado())
    item = ItemVenda.objects.create(venda=venda, item=produto, valor_total_item=produto.valor_unit)
    venda.valor_total = item.valor_total_item
    venda.save()
    
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "lista_produtos.html",
                  {'produtos': produtos,
                   'categorias': categorias,
                   'venda': venda})