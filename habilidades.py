from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']
class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades