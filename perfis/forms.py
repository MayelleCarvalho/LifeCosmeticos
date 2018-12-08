from django.contrib.admin import forms
from django.forms import ModelForm
from django import forms

from perfis.models import Cliente


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'sexo', 'telefone', 'usuario']
        widgets = {'sexo': forms.Select({'class': 'browser-default'}),
                   'usuario': forms.Select({'class': 'browser-default'})}

