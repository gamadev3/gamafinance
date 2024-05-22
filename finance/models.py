from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    class ContaSituacao(models.TextChoices):
        ABERTO = "A", "Aberto"
        PAGO = "P", "Pago"
        VENCIDA = "V", "Vencida"

    nome = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    data_cadastro = models.DateField(auto_now_add=True)
    data_vencimento = models.DateField()
    situacao = models.CharField(
        max_length=1, choices=ContaSituacao, default=ContaSituacao.ABERTO
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cod_barra = models.CharField(max_length=250, default="Não Disponível")
    observacao = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome


class Entrada(models.Model):
    descricao = models.CharField(max_length=400)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self) -> str:
        return self.descricao


class Saida(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    data_pagamento = models.DateField()
