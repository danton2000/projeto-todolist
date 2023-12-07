import json

class Projeto:

    lista_projetos = []

    def __init__(self, nome, descricao, status=0):

        self.__nome = nome

        self.__descricao = descricao

        self.__status = status

        self.__lista_tarefas = None

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

        dict_projeto = {
            'nome': self.__nome,
            'descricao': self.__descricao,
            'status': self.__status
        }

        Projeto.lista_projetos.append(dict_projeto)

        with open("lista_projetos.json", "w") as outfile: 
            json.dump(Projeto.lista_projetos, outfile)

        print("Projeto Adicionado.")

    def removerProjeto(self, index_lista):

        Projeto.lista_projetos.pop(index_lista)

        with open("lista_projetos.json", "w") as outfile: 
            json.dump(Projeto.lista_projetos, outfile)

        print("Projeto Removido.")

    def listarProjetos(self):
        
        #pegando as informações que tem no JSON
        arquivo_projetos = open("lista_projetos.json", "r")

        dic_temp = json.load(arquivo_projetos)

        arquivo_projetos.close()

        return dic_temp

        

projeto = Projeto(nome='projeto1', descricao='descricao do projeto')
projeto = Projeto(nome='projeto2', descricao='descricao do projeto')

#projeto.removerProjeto(0)

projeto.listarProjetos()
    




