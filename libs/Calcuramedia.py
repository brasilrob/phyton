
def media (lista = []):
    if len(lista) == 0:
        return "Nenhum número fornecido."
    total = sum(lista)
    count = len(lista)
    average = total / count
    
    return f"A média dos números fornecidos é: {average}"