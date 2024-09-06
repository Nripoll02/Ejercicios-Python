def promedio_notas(notas_estudiantes):
    promedios = {nombre: sum(notas) / len(notas) for nombre, notas in notas_estudiantes}
    return promedios

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

promedios = promedio_notas(notas_estudiantes)
print(promedios)
