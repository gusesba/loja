from django.contrib import admin
from .models import Produto
from .models import Pessoa
from .models import Venda

# Register your models here.
admin.site.register(Produto)
admin.site.register(Pessoa)
admin.site.register(Venda)