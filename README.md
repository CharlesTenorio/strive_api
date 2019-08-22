# Integração com Cielo via Requests

Requests Python Cielo
[![Build Status](https://travis-ci.org/CharlesTenorio/strive_api.svg?branch=master)](https://travis-ci.org/CharlesTenorio/strive_api)



* [Principais recursos](#principais-recursos)
* [Limitações](#limitações)
* [Exemplo](#exemplo)
    * [Criando um pagamento com cartão de crédito](#criando-um-pagamento-com-cartão-de-crédito)

* [Manual Oficial da Cielo](#manual-oficial-da-cielo)

## Principais recursos

* [x] Pagamentos por cartão de crédito.
## Limitações

Por envolver a interface de usuário da aplicação, funciona apenas como um codigo para criação das transações. Nos casos onde a autorização é direta, não há limitação; mas nos casos onde é necessário a autenticação ou qualquer tipo de redirecionamento do usuário, o desenvolvedor deverá utilizar o SDK para gerar o pagamento e, com o link retornado pela Cielo, providenciar o redirecionamento do usuário.

## Utilizando o SDK
Para criar um pagamento simples com cartão de crédito com o SDK, basta fazer:

## Exemplos
### Criando um pagamento com cartão de crédito

```python

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

## Manual Oficial da Cielo

Para mais informações sobre a integração com a Cielo, vide o manual em: [Integração API 3.0](https://developercielo.github.io/Webservice-3.0/)
