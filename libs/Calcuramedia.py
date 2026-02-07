def media ():
    if len(args) == 0:
        return "Nenhum número fornecido."
    
    total = sum(args)
    count = len(args)
    average = total / count
    
    return f"A média dos números fornecidos é: {average}"