import json

class Projeto:

     lista_projetos = []

     def __init__(self, nome, descricao, status=0):

          self.__nome = nome

          self.__descricao = descricao

          self.__status = status

          self.__tarefas = None
          
          #Colocando os projetos intanciados na lista
          Projeto.lista_projetos.append(self)
          
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
     def tarefas(self):
          return self.__tarefas

     @tarefas.setter
     def tarefas(self, tarefas):
          self.__tarefas = tarefas

     def adicionarProjeto(self):
          
          #Limpando a lista de dicionarios para inserir na lista com os prjetos que estão instanciados.
          lista_dict_projetos = []
          
          for projeto in Projeto.lista_projetos:
               
               dict_projetos = {
                    'nome': projeto.nome,
                    'descricao': projeto.descricao,
                    'status': projeto.status,
                    'tarefas': projeto.tarefas,
               }
               
               lista_dict_projetos.append(dict_projetos)
               
          print(len(lista_dict_projetos))
               
          #Inserindo as informações no Json    
          with open("lista_projetos.json", "w") as outfile: 
               json.dump(lista_dict_projetos, outfile)

          print("Projeto Adicionado.")
        
     @classmethod
     def removerProjeto(cls, index_lista):
          #Utilizando metodo da classe para remover o projeto da lista
          
          Projeto.lista_projetos.pop(index_lista)

          with open("lista_projetos.json", "w") as outfile: 
               json.dump(Projeto.lista_projetos, outfile)

          print("Projeto Removido.")
        
     @classmethod
     def listarProjetos(cls):
          #Utilizando metodo da classe para listar todos os projetos
          
          #Limpar a listar da Classe
          Projeto.lista_projetos = []
          
          #Instanciar os projetos que estão no Json
          
          #pegando as informações que tem no JSON
          arquivo_projetos = open("lista_projetos.json", "r")

          dic_temp = json.load(arquivo_projetos)

          arquivo_projetos.close()
          
          return dic_temp
          
          # for projeto in dic_temp:
               
          #      print(projeto['nome'], projeto['descricao'])
               
          # print(Projeto.lista_projetos)
          
          # #Mostrar os projetos Instanciados
          
          # for projeto in Projeto.lista_projetos:
               
          #      return print(projeto.nome)
          


     
        

        

#projeto = Projeto(nome='projeto1', descricao='descricao do projeto')
#projeto.removerProjeto(0)
#projeto.listarProjetos()
    




