
def registrar_errores(registros) :
    
    jurPosibles = [
    "Buenos Aires", "Caba", "Catamarca", "Chaco", "Chubut",
    "Cordoba", "Corrientes", "Entre Rios", "Formosa", "Jujuy",
    "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen",
    "Rio Negro", "Salta", "San Juan", "San Luis", "Santa Cruz",
    "Santa Fe", "Santiago Del Estero", "Tierra Del Fuego", "Tucuman"
    ]

    registros_erroneos = []
    
    for i, registro in enumerate(registros):
        # Ejemplo de verificación: Chequear si el sexo es M o F
        if registro['sexo'] not in ['M', 'F']:
            registros_erroneos.append((i, registro, "Sexo inválido"))
            
        # Ejemplo de verificación: Chequear si la vacuna es valida
        if registro['vacuna'] not in ['Moderna', 'Sputnik', 'Astrazaneca', 'Sinopharm', 'Pfizer']:
            registros_erroneos.append((i, registro, "Vacuna inválida"))
            
        if registro['jurisdiccion_residencia'] not in jurPosibles:
            registros_erroneos.append((i, registro, "Jurisdiccion invalida"))

        # Verificar valores nulos
        for campo in registro:
            if registro[campo] == '':
                registros_erroneos.append((i, registro, f"{campo} es nulo"))
        
    return registros_erroneos

# Guardar registros erróneos en un archivo

