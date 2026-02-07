import menu
def inserir_num():
    num_inserido = int(input("Inclua um número inteiro na lista:"))
    while True:
        if num_inserido/1 != num_inserido:
            print("O número tem de ser inteiro!")
            num_inserido = int(input("Inclua um número INTEIRO na lista:"))
        else:
            return num_inserido
            break