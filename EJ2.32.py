def publicar(usuario, texto, etiquetas=[], **opciones):
    publicacion = {
        "Usuario": usuario,
        "Texto": texto,
        "Etiquetas": etiquetas
    }
    
    # Agregar las opciones adicionales a la publicación
    publicacion.update(opciones)
    
    return publicacion

# Ejemplo de uso
publicacion = publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)
print(publicacion)
