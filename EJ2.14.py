def analizar_temperaturas(temperaturas):
    if not temperaturas:
        return None, None, None
    
    # Calcular la temperatura media
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    # Encontrar la temperatura máxima y mínima
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima

# Array de temperaturas diarias
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

media, maxima, minima = analizar_temperaturas(temperaturas)

# Mostrar los resultados
print(f"Temperatura media del mes: {media:.2f}")
print(f"Temperatura máxima del mes: {maxima:.2f}")
print(f"Temperatura mínima del mes: {minima:.2f}")
