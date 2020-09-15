from django.shortcuts import render
from .models import Produto
from .models import Pessoa
from .models import Venda
from . import models
from django.db.models import Q


# View Estoque
def home(request):
    # Recebe a pesquisa
    search = request.GET.get('search')

    # Caso seja feita alguma pesquisa data recebe os produtos filtrados, caso contrário recebe todos os produtos
    if (search):
        data = Produto.objects.filter(
            Q(id__icontains=search) | Q(fornecedor__nome__icontains=search) | Q(produto__icontains=search) | Q(
                cor__icontains=search) | Q(marca__icontains=search) | Q(tamanho__icontains=search) | Q(
                valor__icontains=search) | Q(data_recebimento__icontains=search))
    else:
        data = Produto.objects.all()

    # Retorna a página estoque.html e os produtos
    stuff_for_frontend = {'data': data}
    return render(request, 'estoque.html', stuff_for_frontend)


# View new_product
def new_product(request):
    # Recebe os fornecedores do banco de dados
    fornecedores = Pessoa.objects.all()

    # Recebe os parametros do produto preenchidos no formulário
    fornecedor_id = request.POST.get('fornecedor')
    produto = request.POST.get('produto')
    cor = request.POST.get('cor')
    marca = request.POST.get('marca')
    tamanho = request.POST.get('tamanho')
    valor = request.POST.get('valor')
    data_recebimento = request.POST.get('data_recebimento')

    # Caso algum produto tenha sido enviado pelo formulário, cria um novo produto
    if (produto):
        models.Produto.objects.create(fornecedor=fornecedores[int(fornecedor_id) - 1], produto=produto, cor=cor,
                                      marca=marca, tamanho=tamanho, valor=valor, data_recebimento=data_recebimento)

    # Retorna a página new_product.html e os fornecedores
    return render(request, 'new_product.html', {'fornecedores': fornecedores})


# View pessoas
def pessoas(request):
    # Recebe a pesquisa
    search = request.GET.get('search')

    # Caso seja feita alguma pesquisa data recebe as pessoas filtradas, caso contrário recebe todas as pessoas
    if (search):
        data = Pessoa.objects.filter(Q(nome__icontains=search) | Q(telefone__icontains=search))
    else:
        data = Pessoa.objects.all()

    # Retorna a página pessoas.html e as pessoas
    stuff_for_frontend = {'data': data}
    return render(request, 'pessoas.html', stuff_for_frontend)


# View new_pessoa
def new_pessoa(request):
    # Recebe os parametros preenchidos no formulário
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')

    # Caso alguma pessoa tenha sido enviada pelo formulario, criar nova pessoa
    if (nome):
        models.Pessoa.objects.create(nome=nome, telefone=telefone)

    # Retorna a página new_pessoa.html
    return render(request, 'new_pessoa.html')


# View pessoa
def pessoa(request):
    # Recebe o parametro id
    id = request.GET.get('id')

    # Recebe os parametros do formulario
    nome_pessoa = request.POST.get('nome')
    telefone = request.POST.get('telefone')

    # Altera os valores selecionados
    if (request.POST.get('nome_check')):
        models.Pessoa.objects.filter(id=id).update(nome=nome_pessoa)
    if (request.POST.get('telefone_check')):
        models.Pessoa.objects.filter(id=id).update(telefone=telefone)

    # Procura os produtos e a pessoa com o id recebido
    produtos = Produto.objects.filter(fornecedor=id)
    person = Pessoa.objects.get(id=id)

    # Retorna a página pessoa.html e as variáveis person e produtos
    stuff_for_frontend = {'pessoa': person, 'produtos': produtos}
    return render(request, 'pessoa.html', stuff_for_frontend)


# View produto
def produto(request):
    # Recebe o parametro id
    id = request.GET.get('id')

    # Recebe os parametros do formulario
    fornecedor_id = request.POST.get('fornecedor')
    produto_atualizar = request.POST.get('produto')
    cor = request.POST.get('cor')
    marca = request.POST.get('marca')
    tamanho = request.POST.get('tamanho')
    valor = request.POST.get('valor')
    data_recebimento = request.POST.get('data_recebimento')

    # Recebe os fornecedores da base de dados
    fornecedores = Pessoa.objects.all()

    # Altera os valores selecionados
    if (request.POST.get('check')):
        if (fornecedor_id):
            Produto.objects.filter(id=id).update(fornecedor=fornecedores[int(fornecedor_id) - 1])
        if produto_atualizar:
            Produto.objects.filter(id=id).update(produto=produto_atualizar)
        if cor:
            Produto.objects.filter(id=id).update(cor=cor)
        if marca:
            Produto.objects.filter(id=id).update(marca=marca)
        if tamanho:
            Produto.objects.filter(id=id).update(tamanho=tamanho)
        if valor:
            Produto.objects.filter(id=id).update(valor=valor)
        if data_recebimento:
            Produto.objects.filter(id=id).update(data_recebimento=data_recebimento)

    # Procura o produto com o id recebido
    product = Produto.objects.get(id=id)

    # Retorna a página produto.html e as variáveis product e fornecedores
    stuff_for_frontend = {'produto': product, 'fornecedores': fornecedores}
    return render(request, 'produto.html', stuff_for_frontend)


# View vendas
def vendas(request):
    # Recebe a pesquisa
    search = request.GET.get('search')

    # Caso seja feita alguma pesquisa recebe as vendas filtradas, caso contrário recebe todas as vendas
    if (search):
        vendas = Venda.objects.filter(
            Q(produto__id__icontains=search) | Q(produto__fornecedor__nome__icontains=search) | Q(
                produto__produto__icontains=search) | Q(
                produto__cor__icontains=search) | Q(produto__marca__icontains=search) | Q(
                produto__tamanho__icontains=search) | Q(
                produto__valor__icontains=search) | Q(produto__data_recebimento__icontains=search) | Q(
                comprador__nome__icontains=search) | Q(
                data_venda__icontains=search))
    else:
        vendas = Venda.objects.all()

    stuff_for_frontend = {'vendas': vendas}
    return render(request, 'vendas.html', stuff_for_frontend)

def new_venda(request):
    # Retorna a página new_venda.html
    return render(request, 'new_venda.html')
