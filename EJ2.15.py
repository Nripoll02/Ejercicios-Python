def calcular_promedio(*args):
    # Verificar si args no está vacío para evitar división por cero
    if not args:
        return None
    
    # Calcular el promedio de las notas
    promedio = sum(args) / len(args)
    return promedio

# Llamar a la función con un número variable de notas
promedio = calcular_promedio(85, 90, 78, 92)
print(f"El promedio de las notas es: {promedio:.2f}")
