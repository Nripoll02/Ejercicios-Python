def producto_mas_caro(productos):
    # Asegúrate de que la lista no esté vacía
    if not productos:
        return None
    
    # Inicializamos el producto más caro con el primer producto de la lista
    producto_caro = productos[0]
    
    # Recorremos la lista para encontrar el producto más caro
    for producto in productos[1:]:
        # Comparamos el precio de los productos
        if producto[1] > producto_caro[1]:
            producto_caro = producto
    
    return producto_caro

# Lista de productos
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# Llamamos a la función y mostramos el resultado
producto_caro = producto_mas_caro(productos)
print("El producto más caro es:", producto_caro)
