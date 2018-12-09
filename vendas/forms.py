from django.forms import ModelForm
from django import forms
from vendas.models import Produto


class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = ['descricao', 'categoria', 'valor_unit', 'qtd_estoque']
        widgets = {'categoria': forms.Select({'class': 'browser-default'})}