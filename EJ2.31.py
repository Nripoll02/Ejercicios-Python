def calcular_promedio(calificaciones):
    total_calificaciones = sum(calificaciones)
    cantidad_calificaciones = len(calificaciones)
    return total_calificaciones / cantidad_calificaciones

def promedio_general(estudiante):
    total_promedio = 0
    total_materias = 0
    
    for materia, calificaciones in estudiante.items():
        total_promedio += calcular_promedio(calificaciones)
        total_materias += 1
    
    return total_promedio / total_materias

def ranking_estudiantes(estudiantes):
    # Crear una lista de tuplas (ID_estudiante, promedio_general)
    promedios = [(id_estudiante, promedio_general(info)) for id_estudiante, info in estudiantes.items()]
    
    # Ordenar por promedio general de mayor a menor
    ranking = sorted(promedios, key=lambda x: x[1], reverse=True)
    
    return ranking

# Ejemplo de uso
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = ranking_estudiantes(estudiantes)
print(ranking)
