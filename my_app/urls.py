from django.urls import path
from . import views

# Retorna as views para determinadas urls
urlpatterns = [
    path('', views.home, name='home'),
    path('new_product', views.new_product, name='new_product'),
    path('pessoas', views.pessoas, name='pessoas'),
    path('new_pessoa', views.new_pessoa, name='new_pessoa'),
    path('pessoa', views.pessoa, name='pessoa'),
    path('produto', views.produto, name='produto'),
    path('vendas', views.vendas, name='vendas'),
    path('new_venda', views.new_venda, name='new_venda'),
]