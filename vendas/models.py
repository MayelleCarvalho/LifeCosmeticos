from django.db import models

# Create your models here.
from perfis.models import Cliente


class Produto(models.Model):

    img_produto = models.FileField()
    descricao = models.CharField(max_length=100)
    qtd_estoque = models.IntegerField()
    valor_unit = models.FloatField()


class Venda(models.Model):

    data_venda = models.DateField()
    hora_venda = models.TimeField()
    valor_total = models.FloatField()
    produtos = models.ManyToManyField(Produto, through= 'ItemVenda')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')


class ItemVenda(models.Model):

    valor_total_item = models.FloatField()
    qtd_item = models.IntegerField()
    item = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto')
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='venda')





