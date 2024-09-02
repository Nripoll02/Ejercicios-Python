def filtrar_empleados_por_salario(empleados, salario_dado):
    empleados_filtrados = {id: info for id, info in empleados.items() if info[2] > salario_dado}
    return empleados_filtrados

# Diccionario con la información de los empleados
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

# Llamar a la función para filtrar empleados que ganan más de 2800
empleados_filtrados = filtrar_empleados_por_salario(empleados, 2800)
print("Empleados que ganan más de 2800:", empleados_filtrados)
