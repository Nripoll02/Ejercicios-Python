def promedio_calificaciones(registro, matricula):
    if matricula not in registro:
        return None
    
    estudiante = registro[matricula]
    calificaciones = estudiante["calificaciones"]
    
    suma_calificaciones = sum(calificaciones.values())
    numero_materias = len(calificaciones)
    
    if numero_materias == 0:
        return 0
    
    promedio = suma_calificaciones / numero_materias
    return promedio

# Registro de estudiantes
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

# Llamamos a la función y mostramos el promedio de calificaciones para un estudiante específico
matricula = 101
promedio = promedio_calificaciones(estudiantes, matricula)
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es: {promedio:.2f}")
