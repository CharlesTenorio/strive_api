from django.db import models

BANDEIRA_CHOICES = (
        ('Visa', 'Visa'),
        ('Master', 'Master'),
        ('Hipercard', 'Hipercard'),
        ('Hiper', 'Hiper'),
        ('American Express', 'American Express'),
        ('Elo', 'Elo'),
        ('Diners Club', 'Diners Club'),
        ('American Express', 'American Express'),
        ('Discover', 'Discover'),
        ('JCB', 'JCB'),
        ('Aura', 'Aura'),
    )


class ComprarCredito(models.Model):
    id_compra = models.PositiveIntegerField(default=10, blank=True, null=True)
    cliente = models.CharField(max_length=80, blank=True, null=True)
    numero_cartao = models.CharField(max_length=50, blank=True, null=True)
    seguranca = models.CharField(max_length=10, blank=True, null=True)
    bandeira = models.CharField(max_length=80, choices=BANDEIRA_CHOICES)
    validade = models.CharField(max_length=8, null=True, blank=True)
    valor = models.PositiveIntegerField(default=100, blank=True, null=True)
    qtd_parcela = models.PositiveIntegerField(default=1, blank=True, null=True)
    codigo_trasacao = models.CharField(max_length=80, default='0', blank=True, null=True)
    statu_trasacao = models.CharField(max_length=300, blank=True, null=True)
    data_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_compra',)
