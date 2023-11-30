import json

class Projeto:

    lista_projetos = []

    def __init__(self, nome, descricao):

        self.__nome = nome

        self.__descricao = descricao

        self.__lista_tarefas = []

        self.adicionarProjeto()

    @property
    def nome(self):
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return self.__nome

    @nome.setter
    def nome(self, nome):
         # este código é executado sempre que alguém fizer 
         # self.nome = nome
         self.__nome = nome

    @property
    def descricao(self):
         return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
         self.__descricao = descricao

    def adicionarProjeto(self):

        dict_projeto = {
            'nome': self.__nome,
            'descricao': self.__descricao
        }

        Projeto.lista_projetos.append(dict_projeto)

        with open("lista_projeto.json", "w") as outfile: 
            json.dump(Projeto.lista_projetos, outfile)

        print("Projeto Adicionado.")

    def removerProjeto(self, index_lista):

        Projeto.lista_projetos.pop(index_lista)

        with open("lista_projeto.json", "w") as outfile: 
            json.dump(Projeto.lista_projetos, outfile)

        print("Projeto Removido.") 

projeto = Projeto(nome='projeto1', descricao='descricao do projeto')

projeto.removerProjeto(0)

    




