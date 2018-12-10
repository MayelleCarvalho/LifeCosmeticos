from django.db import models

# Create your models here.
from perfis.models import Cliente


class Categoria(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Produto(models.Model):

    img_produto = models.FileField()
    descricao = models.CharField(max_length=100)
    qtd_estoque = models.IntegerField()
    valor_unit = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')


class Venda(models.Model):

    data_venda = models.DateField(null=True, blank=True)
    hora_venda = models.TimeField(null=True, blank=True)
    valor_total = models.FloatField(null=True, blank=True)
    produtos = models.ManyToManyField(Produto, through= 'ItemVenda')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')


class ItemVenda(models.Model):

    valor_total_item = models.FloatField(null=True, blank=True)
    qtd_item = models.IntegerField(null=True, blank=True)
    item = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto')
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='venda')





