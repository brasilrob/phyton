import menu 
def remover_num():
    while True:
        print(menu.lista_num)
        num_apagar = int(input("Escolha um número para apagar:"))
        if num_apagar in menu.lista_num:
            menu.lista_num.remove(num_apagar)
            break
        else:
            print("Esse número não está na lista")