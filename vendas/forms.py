from django.forms import ModelForm

from vendas.models import Produto


class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = ['descricao', 'valor_unit', 'qtd_estoque']