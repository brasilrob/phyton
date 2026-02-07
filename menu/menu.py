from libs.inserir_num import inserir_num
from libs.remover_num import remover_num
from libs.Calcuramedia import media
from libs.soma import soma
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
        inserir_num(lista_num) 
    elif opcao_usuario == 2:
        remover_num(lista_num)

    elif opcao_usuario == 3:
        Calcuramedia()

    elif opcao_usuario == 4:
        soma()

    elif opcao_usuario == 5:
        print(lista_num)

    elif opcao_usuario == 6:
        
        break

    else:
        print("Essa opção não existe.")

print("Você saiu do programa")