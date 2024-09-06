def estadisticas_ventas(ventas_mensuales):
    total_ventas = sum(ventas_mensuales)
    promedio_mensual = total_ventas / len(ventas_mensuales)
    mes_mayor_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1  # Sumar 1 para indicar el mes (1-12)
    
    return {
        "Total de ventas": total_ventas,
        "Promedio mensual": promedio_mensual,
        "Mes con mayores ventas": mes_mayor_ventas
    }

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
estadisticas = estadisticas_ventas(ventas_mensuales)
print(estadisticas)
