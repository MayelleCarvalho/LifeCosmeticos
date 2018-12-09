from django.shortcuts import render, redirect

# Create your views here.
from vendas.forms import ProdutoForm
from vendas.models import Produto, Categoria


def add_produtos(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
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