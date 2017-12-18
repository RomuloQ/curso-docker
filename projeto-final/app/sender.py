# import psycopg2
# import redis
# import json
# import os
from bottle import run, request , route

@route('/', method='POST')

def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    # self.register_message(assunto, mensagem)
    return 'Mensagem enfileirada ! Assunto: {} Mensagem: {}'.format(
        assunto, mensagem
)

if __name__ == '__main__':
    run(host='0.0.0.0',port=8080, debug=True)
    # sender = Sender()
    # sender.run(host='0.0.0.0', port=8080, debug=True)