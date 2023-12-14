from projeto import Projeto

from tarefas import Tarefa

while True:
    print("-- Menu Principal --")
    print("1 - Projetos")
    print("2 - Tarefas")
    print("3 - Criar Usuario")
    print("4 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        # Mostrando os Projetos que foram criados
        print("Projetos:")
        
        for index, projeto in enumerate(Projeto.listarProjetos()):
            
            #Mostrando o nome dos projetos que estão no JSON
            print(index,'-', projeto['nome'])
            
            #Instanciando os Projetos do JSON e colocando as Instancias em uma lista.
            Projeto(nome=projeto['nome'], descricao=projeto['descricao'], status=projeto['status'])

        print("-- Menu | Gerenciamento de Projetos --")
        print("1 - Criar novo Projeto")
        print("2 - Editar status do Projeto")

        opcao = input("Digite uma opção: ")

        if opcao == "1":

            while True:

                # Adicionando um Projeto
                nome = input("Nome do Projeto: ")

                descricao = input("Descrição do Projeto: ")

                projeto = Projeto(nome=nome, descricao=descricao)
                
                projeto.adicionarProjeto()

                continuar = input("Adicionar outro Projeto? (s/n)")

                if continuar == "s":
                    continue
                else:
                    break

        elif opcao == "2":
        
            # Mostrando os Projetos que foram criados
            print("Projetos:")
            
            for index, projeto in enumerate(Projeto.listarProjetos()):
                
                #Mostrando o nome dos projetos que estão no JSON
                print(index,'-', projeto['nome'], projeto['status'])
                
                #Instanciando os Projetos do JSON e colocando as Instancias em uma lista.
                Projeto(nome=projeto['nome'], descricao=projeto['descricao'], status=projeto['status'])

            print("Escolha um projeto para alterar o status:")

            #Escolhendo um Projeto
            index_projeto_escolhido = int(input("Escolha 1 Projeto: "))
            
            projeto_escolhido = Projeto.lista_projetos[index_projeto_escolhido]

            # print(tarefa_escolhida)
            status = int(input("Status:"))
            
            projeto_escolhido.status = status
            
            projeto_escolhido.adicionarProjeto()
            
    elif opcao == "2":
        Tarefa.lista_tarefas = []
        
        # Mostrando os Projetos que foram criados
        print("Projetos:")
        
        for index, projeto in enumerate(Projeto.listarProjetos()):
            
            #Verificar se tem tarefas para fazer as instancias delas e colocar na lista
            if projeto['tarefas'] != None:
                
                for index_tarefa, tarefa in enumerate(projeto['tarefas']):
                    
                    Tarefa(nome=tarefa['nome'], descricao=tarefa['descricao'], status=tarefa['status'])
                    
            
            #Mostrando o nome dos projetos que estão no JSON
            print(index,'-', projeto['nome'])
            
            #Instanciando os Projetos do JSON e colocando as Instancias em uma lista.
            Projeto(nome=projeto['nome'], descricao=projeto['descricao'])

        #Escolhendo um Projeto
        index_projeto_escolhido = int(input("Escolha 1 Projeto: "))
        
        projeto_escolhido = Projeto.lista_projetos[index_projeto_escolhido]
        
        #Mostrando as tarefas e status do projeto escolhido para a edição
        print(f"Tarefas do Projeto {projeto_escolhido.nome}")
        
        tarefas = Tarefa.listaTarefasProjeto(index_projeto_escolhido)
        
        if tarefas != None:
            for index, tarefa in enumerate(tarefas):
            
                print(f"{index} - Tarefa:{tarefa['nome']}, Status: {tarefa['status']}")
                
        print("-- Menu | Gerenciamento de Tarefas --")
        print("1 - Criar nova Tarefa")
        print("2 - Editar status da Tarefa")
        
        opcao = input("Digite uma opção: ")
        
        if opcao == "1":

            while True:
                # Adicionando uma Tarefa
                nome = input("Nome da Tarefa: ")

                descricao = input("Descrição da Tarefa: ")
                
                tarefa = Tarefa(nome=nome, descricao=descricao)
                
                continuar = input("Adicionar outra Tarefa? (s/n)")
                
                if continuar == "s":
                    continue
                else:
                    tarefa = tarefa.adicionarTarefa()
                    # print(Tarefa.lista_tarefas)
                    
                    #Colocando as tarefas no Projeto Escolhido
                    projeto_escolhido.tarefas = tarefa
                    
                    #Enviar para o JSON as alterações no Projeto
                    projeto_escolhido.adicionarProjeto()
                    break
            
        elif opcao == "2":
            if tarefas != None:
                for index, tarefa in enumerate(tarefas):
                
                    print(f"{index} - Tarefa:{tarefa['nome']}, Status: {tarefa['status']}")
                    
                    #Tarefa(nome=tarefa['nome'], descricao=tarefa['descricao'], status = tarefa['status'])
            
            print("Escolha uma tarefa para alterar o status:")
            
            index_tarefa_escolhida = int(input("Escolha 1 Tarefa: "))
            
            tarefa_escolhida = Tarefa.lista_tarefas[index_tarefa_escolhida]
            
            # print(tarefa_escolhida)
            status = int(input("Status:"))
            
            tarefa_escolhida.status = status
            
            # print(len(Tarefa.lista_tarefas))
            
            tarefa_escolhida = tarefa_escolhida.adicionarTarefa()
            
            # print(len(tarefa_escolhida))
            #exit()
            
            #Colocando as tarefas no Projeto Escolhido
            projeto_escolhido.tarefas = tarefa_escolhida
            
            projeto_escolhido.adicionarProjeto()
            
        else:
            break
        
    else:
        pass
