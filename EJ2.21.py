def ordenar_puntuaciones(puntuaciones):
    # Ordenar las tuplas por puntuación de mayor a menor
    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
puntuaciones_ordenadas = ordenar_puntuaciones(puntuaciones)
print(puntuaciones_ordenadas)
