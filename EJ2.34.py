def hacer_reserva(reservas, fecha, nombre, habitacion, precio):
    # Verificar si la habitación ya está reservada en la fecha seleccionada
    if fecha in reservas:
        for reserva in reservas[fecha]:
            if reserva[1] == habitacion:
                return f"Lo siento, la habitación {habitacion} ya está reservada para el {fecha}."
    
    # Si la habitación no está reservada, hacer la reserva
    if fecha not in reservas:
        reservas[fecha] = []
    
    reservas[fecha].append((nombre, habitacion, precio))
    return f"Reserva exitosa para {nombre} en la habitación {habitacion} el {fecha}."

# Ejemplo de uso
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

resultado = hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 150)
print(resultado)
print(reservas)
