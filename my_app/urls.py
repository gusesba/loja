from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_product', views.new_product, name='new_product'),
    path('pessoas', views.pessoas, name='pessoas'),
    path('new_pessoa', views.new_pessoa, name='new_pessoa'),
]