from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class PcInLine(admin.TabularInline):
    model = PC
    extra = 0


class ItemCarrinhoInLine(admin.TabularInline):
    model = ItemCarrinho
    extra = 0


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria')
    list_filter = ('categoria',)

    def get_inline_instances(self, request, obj=None):
        if obj and obj.categoria == 'c':
            return [PcInLine(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)


@admin.register(PC)
class PcAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
    fieldsets = (
        ('PC', {
            'fields': ('cpu','gpu','memoria_ram','motherboard','armazenamento','cooler','fonte','gabinete')
        }),
        ('Produto', {
            'fields': ('produto','id')
        })
    )


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'num_itens_carrinho', 'subtotal_carrinho', 'id')
    inlines = [ItemCarrinhoInLine]


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user')


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'cpf', 'cep', 'foto')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('cpf', 'cep', 'foto')
        }),
    )
