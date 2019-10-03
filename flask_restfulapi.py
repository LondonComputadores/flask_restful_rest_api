from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import ListaHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': '0',
     'nome': 'Alexandre',
     'habilidades' : ['Python', 'Flask']   
    },
    {
     'id': '1',
     'nome': 'Ahlex',
     'habilidades' : ['Python', 'Django']  
    },
    {
     'id': '2',
     'nome': 'Maria',
     'habilidades' : ['Ruby', 'Rails']  
    }
]

#devolve um desenvolvedor pelo id e também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
       try:
           response = desenvolvedores[id]
       except IndexError:
           mensagem = 'Desenvolvedor de ID {} não existe'
           response = {'status':'erro', 'mensagem':mensagem}
       except IndexError:
            mensagem = 'Erro desconhecido. Procure o admin da API'
            response = {'status':'erro', 'mensagem':mensagem}
       return response

    def put(self):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)
        return {'status':'sucesso', 'mensagem': 'Registro Excluido'}

#lista todos os desenvolvedores e permite registar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
        

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)