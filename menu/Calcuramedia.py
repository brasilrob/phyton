def media (*lista_num):
    if len(lista_num) == 0:
        return "Nenhum número fornecido."
    
    total = sum(lista_num)
    count = len(lista_num)
    average = total / count
    
    return f"A média dos números fornecidos é: {average}"