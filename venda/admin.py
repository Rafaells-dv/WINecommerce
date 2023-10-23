from django.contrib import admin
from .models import PC, Produto, InstanciaProduto

# Register your models here.
admin.site.register(PC)
admin.site.register(Produto)
admin.site.register(InstanciaProduto)