def configurar_app(**kwargs):
    # Devolver el diccionario con las configuraciones aplicadas
    return kwargs

# Llamar a la función con configuraciones opcionales
configuraciones = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
print("Configuraciones aplicadas:", configuraciones)
