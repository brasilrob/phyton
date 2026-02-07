import menu
def inserir_num():
    while True:
        num_inserido = int(input("Inclua um número inteiro na lista:"))
        if num_inserido != int:
            print("O número tem de ser inteiro!")
            num_inserido = int(input("Inclua um número INTEIRO na lista:"))
        else:
            return num_inserido
            break