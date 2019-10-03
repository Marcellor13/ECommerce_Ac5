from django.db import models


class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.codigo[:20]


class Orcamento(models.Model):
    cod_orcamento = models.IntegerField()
    data = models.DateField()
    status = models.IntegerField()
    valor_total = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return str(self.pk)


class ItemOrcamento(models.Model):
    codigo_item = models.IntegerField()
    codigo_orcamento = models.IntegerField()
    codigo_produto = models.IntegerField()
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)
    valor_unitario = models.DecimalField(
        max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return str(self.pk)
