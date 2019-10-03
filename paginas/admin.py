from django.contrib import admin
from .models import Produto
from .models import Orcamento
from .models import ItemOrcamento

admin.site.register(Produto)
admin.site.register(Orcamento)
admin.site.register(ItemOrcamento)
