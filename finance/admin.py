from django.contrib import admin
from finance.models import Categoria, Conta, Entrada, Saida


# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
    )
    search_fields = ("nome",)


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "valor",
        "data_cadastro",
        "data_vencimento",
        "situacao",
        "categoria",
    )
    search_fields = ("nome",)
    list_filter = (
        "data_cadastro",
        "data_vencimento",
        "categoria",
        "situacao",
    )


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = (
        "descricao",
        "valor",
        "data",
    )
    search_fields = ("descricao",)


@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = (
        "conta",
        "data_pagamento",
    )
    search_fields = ("conta",)
    list_filter = ("data_pagamento",)
