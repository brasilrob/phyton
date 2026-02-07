import menu
def media ():
    if len(menu.lista_num) == 0:
        return "Nenhum número fornecido."
    total = sum(menu.lista_num)
    count = len(menu.lista_num)
    average = total / count
    
    return f"A média dos números fornecidos é: {average}"