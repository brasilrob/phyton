import menu 
def remover_num(remover):
    while True:
        print(menu.lista_num)
        num_apagar = int(input("Escolha um número para apagar:"))
        if num_apagar in remover:
            return num_apagar
            break
        else:
            print("Esse número não está na lista")