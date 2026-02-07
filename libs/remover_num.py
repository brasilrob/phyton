
def remover_num(lista = []):
    while True:
        print(lista)
        num_apagar = int(input("Escolha um número para apagar:"))
        if num_apagar in lista:
            return num_apagar
            break
        else:
            print("Esse número não está na lista")