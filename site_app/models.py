from django.db import models

# Create your models here.
class Pessoa(models.Model):
    """class Pessoa
    -
    Fieds:
    - `nome` = String
    - `email` String
    - `idade` = Int"""
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.IntegerField()