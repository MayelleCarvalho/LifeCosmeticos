from django.db import models

# Create your models here.
class Produto(models.Model):

    descricao = models.CharField(max_length=100)
    qtd_estoque = models.IntegerField()
    valor_unit = models.FloatField()
