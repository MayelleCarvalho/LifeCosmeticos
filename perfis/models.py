from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(max_length=255, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    telefone = models.CharField(max_length=255)

    usuario = models.OneToOneField(User, related_name='cliente')
