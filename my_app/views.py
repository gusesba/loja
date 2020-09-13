from django.shortcuts import render
from .models import Produto
from .models import Pessoa
from . import models

# Create your views here.
def home(request):
    data = Produto.objects.all()
    stuff_for_frontend = {'data':data}
    return render(request, 'estoque.html', stuff_for_frontend)

def new_product(request):
    fornecedores = Pessoa.objects.all()
    fornecedor_id = request.POST.get('fornecedor')
    produto = request.POST.get('produto')
    cor = request.POST.get('cor')
    marca = request.POST.get('marca')
    tamanho = request.POST.get('tamanho')
    valor = request.POST.get('valor')
    data_recebimento = request.POST.get('data_recebimento')
    if(produto):
        models.Produto.objects.create(fornecedor=fornecedores[int(fornecedor_id)-1], produto=produto, cor=cor, marca=marca, tamanho=tamanho, valor=valor, data_recebimento=data_recebimento)
    return render(request, 'new_product.html', {'fornecedores':fornecedores})


def pessoas(request):
    data = Pessoa.objects.all()
    stuff_for_frontend = {'data': data}
    return render(request, 'pessoas.html', stuff_for_frontend)


def new_pessoa(request):
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    if(nome):
        models.Pessoa.objects.create(nome=nome, telefone=telefone)
    return render(request, 'new_pessoa.html')