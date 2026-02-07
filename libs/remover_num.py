import menu 
def remover_num():
    while True:
        print(lista)
        num_apagar = int(input("Escolha um número para apagar:"))
        if num_apagar in menu.lista_num:
            return num_apagar
            break
        else:
            print("Esse número não está na lista")