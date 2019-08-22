from decouple import config
import requests
import json
import logging

loogger = logging.getLogger('erro_cielo')
url_prd = config('CIELO_PRD_PUT_POST')
id_cliente = config('MERCHANT_ID')
key_cliente = config('MERCHANT_KEY')


def comprar_credito(id_compra, cliente, numero_cartao, seguranca, bandeira, validade, valor, qtd_parcela):
    try:
        headers = {'Content-Type': 'application/json', 'MerchantId': id_cliente, 'MerchantKey': key_cliente}
        data = {
            "MerchantOrderId": id_compra,
            "Customer": {"Name": cliente},
            "Payment": {"Type": "CreditCard", "Amount": valor, "Installments": qtd_parcela,
                        "SoftDescriptor": "123456789ABCD",
                        "CreditCard": {"CardNumber": numero_cartao, "Holder": cliente,
                                       "ExpirationDate": validade, "SecurityCode": seguranca, "Brand": bandeira},
                        "IsCryptoCurrencyNegotiation": True
                        }
        }

        r = requests.post(url_prd + '1/sales/', data=json.dumps(data), headers=headers)
        resposa = r.json()
        codigo_transacao = resposa["Payment"]["Tid"]
        msg_retorno = resposa["Payment"]["ReturnMessage"]
        print(r.status_code)
        return msg_retorno, codigo_transacao
    except Exception as e:
        print(e)
