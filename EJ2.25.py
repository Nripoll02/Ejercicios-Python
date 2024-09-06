def analizar_finanzas(**finanzas):
    balance_final = sum(finanzas.values())
    return balance_final

balance = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"Balance final: {balance}")
