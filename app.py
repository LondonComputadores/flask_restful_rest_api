from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
    }
]

#devolve um desenvolvedor pelo id e também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=(['GET','PUT', 'DELETE']))
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'
            response = {'status':'erro', 'mensagem':mensagem}
        except IndexError:
            mensagem = 'Erro desconhecido. Procure o admin da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem': 'Registro Excluido'})

#lista todos os desenvolvedores e permite registar um novo desenvolvedor
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug=True)