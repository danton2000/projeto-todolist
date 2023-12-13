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

          #Colocando as tarefas intanciadas na lista
          Tarefa.lista_tarefas.append(self)

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

     def adicionarTarefa(self):

          lista_dict_tarefas = []
          
          data_atual = date.today()
          
          print(len(Tarefa.lista_tarefas))
          
          for tarefa in Tarefa.lista_tarefas:
               
               dict_tarefas = {
                    'nome': tarefa.nome,
                    'descricao': tarefa.descricao,
                    'status': tarefa.status,
                    'data_cricao': data_atual.strftime("%d/%m/%Y"),
                    'data_finalizacao': tarefa.data_finalizacao
               }
               
               lista_dict_tarefas.append(dict_tarefas)
          
          return lista_dict_tarefas
     
     @classmethod
     def listaTarefasProjeto(cls, index_projeto):
          
          arquivo_projetos = open("lista_projetos.json", "r")

          dic_temp = json.load(arquivo_projetos)

          arquivo_projetos.close()
          
          return dic_temp[index_projeto]["tarefas"]

#tarefa = Tarefa(nome='projeto1', descricao='descricao do projeto')
    




