from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey('Pessoa', on_delete=models.PROTECT)
    produto = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=10)
    valor = models.FloatField()
    data_recebimento = models.DateField()

    def __str__(self):
        return '{}'.format(self.id)

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nome)

class Venda(models.Model):
    produto = models.OneToOneField('Produto', on_delete=models.PROTECT, primary_key=True)
    comprador = models.ForeignKey('Pessoa', on_delete=models.PROTECT)
    data_venda = models.DateField()

    def __str__(self):
        return '{} | {} | {}'.format(self.comprador, self.produto, self.produto.fornecedor)
