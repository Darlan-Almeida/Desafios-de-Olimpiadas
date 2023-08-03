def navegacao( hpa_aviao , lat , lng):
    hpa_ponto = 1013
    pes = 30.48
    metros_reducao = (30 * pes) / 100
    distancia = (hpa_ponto - hpa_aviao) * metros_reducao
    return distancia
    
print(navegacao( 782 , 0 , 0))


print((-6.782159 - -6.787979))