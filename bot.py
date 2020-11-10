import requests

URL_TELEGRAM_BASE = "https://api.telegram.org/bot1439216922:AAF2nwOKWl05rGDxgSqwnxf4AAJjjtXMafs"


resposta = requests.post(URL_TELEGRAM_BASE + "/getUpdates")
resposta = resposta.json()


for item in resposta['result']:
    if 'photo' in item['message']:
        print('Foto Encontrada!')
    else:
        conteudo = {
            'chat_id': item['message']['chat']['id'],
            'text': 'Por favor, enviar somente imagens.',
            'reply_to_message_id': item['message']['message_id']
        }
        requests.post(URL_TELEGRAM_BASE + "/sendMessage", data=conteudo)
        print("Imagem encontrada")

#Dois problemas:
#   O bot responde todas as mensagens que estão no chat
#   Necessidade de ficar executando o bot toda hora

#https://www.youtube.com/watch?v=-s58ABCv6J4&ab_channel=C%C3%B3digoEscola
