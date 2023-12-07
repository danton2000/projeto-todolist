import json

#utilizando a lib date para manipulaçao de datas no Python
from datetime import date

class Tarefa:

    lista_tarefas = []

    def __init__(self, nome, descricao, status=0):

        self.__nome = nome

        self.__descricao = descricao

        self.__status = status

        self.__data_criacao = None

        self.__data_finalizacao = None

        self.adicionarTarefaProjeto()

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

    @property
    def status(self):
         return self.__status

    @status.setter
    def status(self, status):
         self.__status = status

    @property
    def data_criacao(self):
         return self.__data_criacao

    @data_criacao.setter
    def data_criacao(self, data_criacao):
         self.__data_criacao = data_criacao

    @property
    def data_finalizacao(self):
         return self.__data_finalizacao

    @data_finalizacao.setter
    def data_finalizacao(self, data_finalizacao):
         self.__data_finalizacao = data_finalizacao

    def adicionarTarefaProjeto(self):

        data_atual = date.today()

        dict_tarefa = {
            'nome': self.__nome,
            'descricao': self.__descricao,
            'status': self.__status,
            'data_cricao': data_atual.strftime("%d/%m/%Y"),
            'data_finalizacao': self.__data_finalizacao
        }

        Tarefa.lista_tarefas.append(dict_tarefa)

        return Tarefa.lista_tarefas

#tarefa = Tarefa(nome='projeto1', descricao='descricao do projeto')
    




