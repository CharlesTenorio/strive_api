import json
import logging
from cieloApi3 import Environment
from cieloApi3 import Merchant
from cieloApi3 import Sale
from cieloApi3 import Customer
from cieloApi3 import CreditCard
from cieloApi3 import CieloEcommerce
from cieloApi3 import Payment
from decouple import config


loogger = logging.getLogger('erro_cielo')
url_prd = config('CIELO_PRD_PUT_POST')
id_cliente = config('MERCHANT_ID')
key_cliente = config('MERCHANT_KEY')
id_cliente_hoodid = config('MERCHANT_ID_HOODID')
key_cliente_hoodid = config('MERCHANT_KEY_HODID')

environment = Environment(sandbox=False)

merchant = Merchant(id_cliente, key_cliente)


def comprar_credito(id_compra, cliente, numero_cartao, seguranca, bandeira, validade, valor, qtd_parcela):
    msg_retorno = ''
    codigo_transacao = ''
    x = ''

    try:
        sale = Sale(id_compra)
        sale.customer = Customer(cliente)
        credit_card = CreditCard(seguranca, bandeira)
        credit_card.expiration_date = validade
        credit_card.security_code = seguranca
        credit_card.card_number = numero_cartao
        credit_card.holder = cliente
        sale.payment = Payment(valor)
        sale.payment.credit_card = credit_card
        sale.payment.installments = qtd_parcela
        cielo_ecommerce = CieloEcommerce(merchant, environment)
        response_create_sale = cielo_ecommerce.create_sale(sale)
        x = json.dumps(response_create_sale, indent=3, sort_keys=True)
        # payment_id = sale.payment.payment_id
        resultado = json.loads(x)
        codigo_transacao = resultado["Payment"]["Tid"]
        msg_retorno = resultado["Payment"]["ReturnMessage"]

    except KeyError as e:
        print(e)

    return (msg_retorno, codigo_transacao)
