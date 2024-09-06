from collections import Counter

def analizar_encuestas(encuestas):
    resultados = {}
    
    for pregunta, respuestas in encuestas.items():
        frecuencia_respuestas = dict(Counter(respuestas))
        resultados[pregunta] = frecuencia_respuestas
    
    return resultados

# Ejemplo de uso
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultados_encuestas = analizar_encuestas(encuestas)
print(resultados_encuestas)
