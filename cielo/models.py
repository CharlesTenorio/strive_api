from django.db import models


class ComprarCredito(models.Model):
    valor = models.DecimalField(max_digits=11, decimal_places=3)
    qtd_parcela = models.PositiveIntegerField(default=1, blank=True, null=True)
    codigo_trasacao = models.CharField(max_length=80, default='0', blank=True, null=True)
    statu_trasacao = models.CharField(max_length=300, blank=True, null=True)
    data_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_compra',)
