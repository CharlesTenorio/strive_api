from django.test import TestCase
from decouple import config
from cielo.api.funcao import comprar_credito


class TestCielo(TestCase):
    def test_url_producao_post(self):
        url = config('CIELO_PRD_PUT_POST')
        assert url == 'https://api.cieloecommerce.cielo.com.br/'

    def test_url_producao_get(self):
        url = config('CIELO_PRD_GET')
        assert url == 'https://apiquery.cieloecommerce.cielo.com.br/'

    def test_compra_autorizada(self):
        resposta_cielo, trasacao = comprar_credito(10, 'Martoele C. Pixão', '0662821825086128', '279',
                                                   'HiperCard', '07/2020', 200, 1)

        assert resposta_cielo == 'Autorizacao negada'
