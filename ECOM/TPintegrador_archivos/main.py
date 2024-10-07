from registrar_errores import *

#Análisis de datos de vacunación COVID-19 sin librerías externas

def listarRegistros(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8' al leer el archivo
        # Leer la primera línea para obtener los encabezados
        encabezados = f.readline().strip().split(',')
        datos = []
        for linea in f:
            fila = linea.strip().split(',')
            datos.append(dict(zip(encabezados, fila)))  # Combina encabezados con valores
    return datos

# Cargar archivos
reg1 = listarRegistros('base1.csv')  # Carga datos de un archivo CSV en una lista de diccionarios.
reg2 = listarRegistros('base2.csv')  # Carga datos de un archivo CSV en una lista de diccionarios.

registros = reg1 + reg2  # Uniendo ambas listas

# Identificar registros erroneos 

with open('registros_erroneos.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8' al escribir el archivo
        f.write('Índice,Registro,Observación\n')
        for indice, registro, observacion in registrar_errores(registros):
            f.write(f"{indice},{registro},{observacion}\n")


distribucion_genero = {'M': 0, 'F': 0}

for registro in registros:
    sexo = registro['sexo']  # Obtiene el sexo del registro
    # Verifica si el sexo es válido antes de intentar incrementar
    if sexo in distribucion_genero:
        distribucion_genero[sexo] += 1

# Vacunas aplicadas por tipo de vacuna: ¿Que cantidad de personas han recibido cada de las vacunas?
distribucion_vacunas = {'Moderna': 0, 'Sputnik': 0, 'Astrazeneca': 0, 'Sinopharm': 0, 'Pfizer': 0}

for registro in registros:
    vacuna = registro['vacuna']
    if vacuna in distribucion_vacunas:
        distribucion_vacunas[vacuna] += 1

# Calcular proporciones
total_vacunas = sum(distribucion_vacunas.values())

# Guardar la distribución por género
with open('distribucion_genero.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Sexo,Cantidad\n')
    for sexo, cantidad in distribucion_genero.items():
        f.write(f"{sexo},{cantidad}\n")

# Guardar la distribución de vacunas
with open('distribucion_vacunas.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Vacuna,Cantidad,Proporción\n')
    for vacuna, cantidad in distribucion_vacunas.items():
        proporcion = (cantidad / total_vacunas) * 100 
        f.write(f"{vacuna},{cantidad},{round(proporcion)}%\n")

# Dosis por jurisdicción de residencia: ¿Cuantas personas han diso vacunadas en cada provincia?

dosis_por_jurisdiccion = {"Buenos Aires": 0, "CABA": 0, "Catamarca": 0, "Chaco": 0, "Chubut": 0, "Córdoba": 0, "Corrientes": 0, "Entre Ríos": 0, "Formosa": 0, "Jujuy": 0, "La Pampa": 0, "La Rioja": 0, "Mendoza": 0, "Misiones": 0, "Neuquén": 0, "Río Negro": 0, "Salta": 0, "San Juan": 0, "San Luis": 0, "Santa Cruz": 0, "Santa Fe": 0, "Santiago del Estero": 0, "Tierra del Fuego": 0, "Tucumán": 0}


for registro in registros:
    jurisdiccion = registro['jurisdiccion_residencia']
    if jurisdiccion in dosis_por_jurisdiccion:
        dosis_por_jurisdiccion[jurisdiccion] += 1

# Guardar dosis por jurisdicción
with open('dosis_por_jurisdiccion.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Jurisdicción,Cantidad\n')
    for jurisdiccion, cantidad in dosis_por_jurisdiccion.items():
        f.write(f"{jurisdiccion},{cantidad}\n")

# ¿Cuántas personas han recibido la segunda dosis en cada provincia?
segunda_dosis = {"Buenos Aires": 0, "CABA": 0, "Catamarca": 0, "Chaco": 0, "Chubut": 0, "Córdoba": 0, "Corrientes": 0, "Entre Ríos": 0, "Formosa": 0, "Jujuy": 0, "La Pampa": 0, "La Rioja": 0, "Mendoza": 0, "Misiones": 0, "Neuquén": 0, "Río Negro": 0, "Salta": 0, "San Juan": 0, "San Luis": 0, "Santa Cruz": 0, "Santa Fe": 0, "Santiago del Estero": 0, "Tierra del Fuego": 0, "Tucumán": 0}

for registro in registros:
    if registro['nombre_dosis_generica'] == '2da':
        jurisdiccion = registro['jurisdiccion_residencia']
        if jurisdiccion  in segunda_dosis:
            segunda_dosis[jurisdiccion] += 1

# Guardar segunda dosis por jurisdicción
with open('segunda_dosis_por_jurisdiccion.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Jurisdicción,Cantidad\n')
    for jurisdiccion, cantidad in segunda_dosis.items():
        f.write(f"{jurisdiccion},{cantidad}\n")

# Cuántas personas mayores de 60 años han recibido dosis de refuerzo
refuerzos_mayores_60 = sum(1 for registro in registros
                            if registro['orden_dosis'] > '2' and
                            '60' in registro['grupo_etario'])

# Guardar información sobre refuerzos mayores de 60
with open('refuerzos_mayores_60.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Cantidad\n')
    f.write(f"{refuerzos_mayores_60}\n")


# Mostrar resultados en la consola

print("Análisis completado.\n")

print("Distribución por Género:")
print(f"Masculino: {distribucion_genero['M']}")
print(f"Femenino: {distribucion_genero['F']}\n")  # Salto de línea añadido

print("Vacunas Aplicadas por Tipo de Vacuna:")
for vacuna, cantidad in distribucion_vacunas.items():
    proporcion = (cantidad / total_vacunas) * 100
    print(f"{vacuna}: {round(proporcion)}%")
print()  # Salto de línea añadido

print("Dosis por Jurisdicción:")
for jurisdiccion, cantidad in dosis_por_jurisdiccion.items():
    if cantidad != 0:
        print(f"{jurisdiccion}: {cantidad}")
print()  # Salto de línea añadido

print("Segunda Dosis por Jurisdicción:")
for jurisdiccion, cantidad in segunda_dosis.items():
    if cantidad != 0:
        print(f"{jurisdiccion}: {cantidad}")
print()  # Salto de línea añadido

print(f"Personas mayores de 60 años que recibieron dosis de refuerzo: {refuerzos_mayores_60}")
print()