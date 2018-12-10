from django.forms import ModelForm
from django import forms
from vendas.models import Produto


class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = ['descricao', 'categoria', 'valor_unit', 'img_produto', 'qtd_estoque']
        widgets = {'categoria': forms.Select({'class': 'browser-default'})}

    def clean(self):
        cleaned_data = super().clean()
        qtd_estoque = cleaned_data.get("qtd_estoque")

        if qtd_estoque <= 0:
            self.add_error('qtd_estoque', "Quantidade em estoque inválida!")