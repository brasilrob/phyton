import libs
lista_num = []

while True :
    print("------MENU------")
    print("1- Incluir número na lista")
    print("2- Remover número da lista")
    print("3- Calcular média da lista")
    print("4- Calcular somatório")
    print("5- Imprimir lista")
    print("6- Sair")

    opcao_usuario = int(input(""))

    if opcao_usuario == 1:
        lista_num.append(libs.inserir_num()) 
    elif opcao_usuario == 2:
        lista_num.remove(libs.remover_num())

    elif opcao_usuario == 3:
        libs.media()

    elif opcao_usuario == 4:
        libs.soma()
        
    elif opcao_usuario == 5:
        print(lista_num)

    elif opcao_usuario == 6:
        
        break

    else:
        print("Essa opção não existe.")

print("Você saiu do programa")