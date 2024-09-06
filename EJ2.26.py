def registro_empleado(nombre, edad, salario, **otros_datos):
    # Crear un diccionario con los datos obligatorios
    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario
    }
    
    # Agregar los datos adicionales recibidos en **kwargs
    empleado.update(otros_datos)
    
    return empleado

# Ejemplo de uso
empleado = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
print(empleado)
