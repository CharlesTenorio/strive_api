from rest_framework.serializers import ModelSerializer
from cielo.models import ComprarCredito


class CompraCreditoSerializer(ModelSerializer):
    class Meta:
        model = ComprarCredito
        fields = ['id', 'id_compra', 'cliente', 'numero_cartao', 'seguranca', 'bandeira', 'validade',
                  'valor', 'qtd_parcela', 'codigo_trasacao', 'statu_trasacao', 'data_compra']
