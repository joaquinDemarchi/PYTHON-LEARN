
def dividirXGenero(registros):
    distribucion_genero = {'M': 0, 'F': 0}

    for registro in registros:
        sexo = registro['sexo']  # Obtiene el sexo del registro
        # Verifica si el sexo es válido antes de intentar incrementar
        if sexo in distribucion_genero:
            distribucion_genero[sexo] += 1
    
    return distribucion_genero
    