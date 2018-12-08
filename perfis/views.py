from django.shortcuts import render, redirect

# Create your views here.
from perfis.forms import ClienteForm


def index(request):
    return render(request, 'base.html')


def add_perfil(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ClienteForm()
        return render(request, 'add_perfil.html',
                      {'form': form})