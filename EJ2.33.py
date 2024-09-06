def simular_ventas(*ventas):
    total_ingresos = sum(cantidad * precio_por_unidad for _, cantidad, precio_por_unidad in ventas)
    return total_ingresos

# Ejemplo de uso
ingresos_totales = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
print(ingresos_totales)
