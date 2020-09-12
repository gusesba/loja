from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor = models.CharField(max_length=30)
    produto = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=10)
    valor = models.FloatField()
    data_recebimento = models.DateField()

    def __str__(self):
        return '{}'.format(self.id)
