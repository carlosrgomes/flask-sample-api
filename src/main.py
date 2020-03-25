from flask import Flask, Response, request
import requests
import json
import xmltodict
import mimetypes
#import sckilearn


app = Flask(__name__)

url = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"



@app.route("/news/<formatresponse>")
def news(formatresponse):
    #logica de ler o picle e carregar o modelo no sckitlear
    retorno = 'formato nao suportado'
    mimetypes_retorno = ''
    if formatresponse == 'xml':
       retorno = get_news()
       mimetypes_retorno = mimetypes.types_map['.xml']
    if formatresponse == 'json':
        retorno = json.dumps(xmltodict.parse(get_news()))
        mimetypes_retorno = mimetypes.types_map['.json']

    return Response(retorno, mimetype=mimetypes_retorno)

def get_news():
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    myxml = response.text
    return myxml


if __name__ == "__main__":
    app.run(host='0.0.0.0')
