def configurar_perfiles(usuarios, **configuraciones):
    perfiles = {usuario: list(configuraciones.items()) for usuario in usuarios}
    return perfiles

usuarios = ["Ana", "Luis", "María"]
perfiles_configurados = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(perfiles_configurados)
