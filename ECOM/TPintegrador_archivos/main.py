from registrar_errores import *
from dividirXGenero import *
from dividirXTipVacuna  import *
from dosisXJurisdiccion  import *
from segDosisXJur  import *
from refuerzosAMas60  import *

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


with open('genero.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Sexo,Cantidad\n')
    for sexo, cantidad in dividirXGenero(registros).items():
        f.write(f"{sexo},{cantidad}\n")

# Vacunas aplicadas por tipo de vacuna: ¿Que cantidad de personas han recibido cada de las vacunas?

total_vacunas = sum(dividirXTipVacuna(registros).values())

# Guardar la distribución de vacunas
with open('tipos_vacunas.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Vacuna,Cantidad,Proporción\n')
    for vacuna, cantidad in dividirXTipVacuna(registros).items():
        proporcion = (cantidad / total_vacunas) * 100 
        f.write(f"{vacuna},{cantidad},{round(proporcion)}%\n")

# Dosis por jurisdicción de residencia: ¿Cuantas personas han diso vacunadas en cada provincia?

with open('dosis_por_jurisdiccion.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
        f.write('Jurisdicción,Cantidad\n')
        for jurisdiccion, cantidad in dosisXJurisdiccion(registros).items():
            f.write(f"{jurisdiccion},{cantidad}\n")

# ¿Cuántas personas han recibido la segunda dosis en cada provincia?

# Guardar segunda dosis por jurisdicción
with open('segunda_dosis_por_jurisdiccion.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Jurisdicción,Cantidad\n')
    for jurisdiccion, cantidad in segDosisXJur(registros).items():
        f.write(f"{jurisdiccion},{cantidad}\n")

# Cuántas personas mayores de 60 años han recibido dosis de refuerzo



with open('refuerzos_mayores_60.csv', 'w', encoding='utf-8') as f:  # Asegúrate de usar 'utf-8'
    f.write('Cantidad\n')
    f.write(f"{refuerzosAMas60(registros)}\n")




print("Análisis completado.\n")

print("Distribución por Género:")
print(f"Masculino: {dividirXGenero(registros)['M']}")
print(f"Femenino: {dividirXGenero(registros)['F']}\n")  

print("Vacunas Aplicadas por Tipo de Vacuna:")
for vacuna, cantidad in dividirXTipVacuna(registros).items():
    proporcion = (cantidad / total_vacunas) * 100
    print(f"{vacuna}: {round(proporcion)}%")
print()  # Salto de línea añadido

print("Dosis por Jurisdicción:")
for jurisdiccion, cantidad in dosisXJurisdiccion(registros).items():
    if cantidad != 0:
        print(f"{jurisdiccion}: {cantidad}")
print()  # Salto de línea añadido

print("Segunda Dosis por Jurisdicción:")
for jurisdiccion, cantidad in segDosisXJur(registros).items():
    if cantidad != 0:
        print(f"{jurisdiccion}: {cantidad}")
print()  # Salto de línea añadido

print(f"Personas mayores de 60 años que recibieron dosis de refuerzo: {refuerzosAMas60(registros)}")
print()