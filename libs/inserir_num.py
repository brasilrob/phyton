import menu
def inserir_num():
    while True:
        num_inserido = int(input("Inclua um número inteiro na lista:"))
        if num_inserido != int:
            print("O número tem de ser inteiro!")
            num_inserido = int(input("Inclua um número INTEIRO na lista:"))
        else:
            menu.lista_num.append = num_inserido
            break