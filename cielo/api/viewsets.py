from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cielo.models import ComprarCredito
from .serializers import CompraCreditoSerializer
from .funcao import comprar_credito


class CompraViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ComprarCredito.objects.all()
    serializer_class = CompraCreditoSerializer

    def create(self, request, *args, **kwargs):
        msg, transacao = comprar_credito(request.data.get('id_compra'), request.data.get('cliente'),
                                         request.data.get('numero_cartao'), request.data.get('seguranca'),
                                         request.data.get('bandeira'), request.data.get('validade'),
                                         request.data.get('valor'),
                                         request.data.get('qtd_parcela'))

        return Response({'msg': msg, 'trasacao': transacao})


class HoodidViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ComprarCredito.objects.all()
    serializer_class = CompraCreditoSerializer

    def create(self, request, *args, **kwargs):
        msg, transacao = comprar_credito(request.data.get('id_compra'), request.data.get('cliente'),
                                         request.data.get('numero_cartao'), request.data.get('seguranca'),
                                         request.data.get('bandeira'), request.data.get('validade'),
                                         request.data.get('valor'), request.data.get('qtd_parcela'))

        return Response({'msg': msg, 'trasacao': transacao})
