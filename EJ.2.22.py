def calcular_precio_total(paquetes):
    precios_totales = {}
    for destino, precio, duracion in paquetes:
        precios_totales[destino] = precio * duracion
    return precios_totales

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

precios_totales = calcular_precio_total(paquetes)
print(precios_totales)
