def procesar_ventas(ventas_diarias):
    if not ventas_diarias:
        return 0, 0
    
    total_ventas = sum(ventas_diarias)
    
    # Calcular el promedio de ventas por día
    promedio_ventas = total_ventas / len(ventas_diarias)
    
    return total_ventas, promedio_ventas

# Array de ventas diarias
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

# Llamar a la función y mostrar los resultados
total, promedio = procesar_ventas(ventas_diarias)
print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio:.2f}")
