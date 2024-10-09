def refuerzosAMas60(registros):

    refuerzos_mayores_60 = 0
    
    for registro in registros:
        if registro['orden_dosis'] > '2' and '60' in registro['grupo_etario']:
            refuerzos_mayores_60 += 1
            
    return refuerzos_mayores_60

