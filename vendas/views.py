from django.shortcuts import render, redirect

# Create your views here.
from vendas.forms import ProdutoForm
from vendas.models import Produto, Categoria


def add_produtos(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ProdutoForm()
        return render(request, 'add_produtos.html',
                      {'form': form})


def lista_produtos(request):

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "lista_produtos.html", {'produtos' : produtos, 'categorias': categorias})


def detalhar_produto(request, produto_id):

    produto = Produto.objects.get(id=produto_id)
    return render(request, 'detalhar_produto.html',
                  {'produto': produto})


def editar_produto(request, produto_id):

    produto = Produto.objects.get(id=produto_id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ProdutoForm(instance=produto)

        return render(request, "editar_produto.html",
                      {'form': form})