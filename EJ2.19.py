def analizar_resultados(resultados):
    total_goles_anotados = 0
    total_goles_recibidos = 0
    
    # Recorrer el diccionario para sumar los goles
    for goles_anotados, goles_recibidos in resultados.values():
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos
    
    return total_goles_anotados, total_goles_recibidos

# Diccionario con los resultados de los partidos
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

# Llamar a la función y mostrar los resultados
total_anotados, total_recibidos = analizar_resultados(resultados)
print(f"Total de goles anotados: {total_anotados}")
print(f"Total de goles recibidos: {total_recibidos}")
