import menu 
 def remover_num()
    while True:
        print(lista_num)
        num_apagar = int(input("Escolha um número para apagar:"))
        if num_apagar in lista_num:
            lista_num.remove(num_apagar)
        else:
            print("Esse número não está na lista")