def q1(cidades):

    cidade = [i for i in cidades.keys()]
    idade = [i for i in cidades.values()]
    resultado = []

    for index , i in enumerate(idade):
        if(i > 100):
            resultado.append(cidade[index])

    return(resultado)

def q2(lista1, lista2):
    resultado = 0
    lista_resultado = []



    for i in lista1:
        if(i > 0):
            resultado += i
            lista_resultado.append(i)
    for i in lista2:
        if(i > 0):
            resultado += i
            lista_resultado.append(i)
            
    lista_resultado.sort()

    return resultado,lista_resultado


def ler_valores():
    nums = [ ]
    num = None
    while(num != 0):
        num = int(input("digite um número: "))
        if(num != 0):
            nums.append(num)
        
    return nums

def q3():
    valores = ler_valores()
    pares = [ ]
    impares = []

    for i in valores:
        if( i % 2 == 0):
            pares.append(i)
            
        else:
            impares.append(i)
            
            
    return(pares, impares)



def ler_alturas():
    lista_altura = []
    for i in range(3):
        altura = float(input("digite a altura: "))
        lista_altura.append(altura)
    return lista_altura
        

def q4():
    lista_altura = ler_alturas()
    primeiro = 0 
    segundo = 0
    terceiro = 0
        
    primeiro = max(lista_altura)
    lista_altura.remove(primeiro)
    
    if(lista_altura[0] > lista_altura[1]):
        segundo = lista_altura[0]
        terceiro = lista_altura[1]
    else:
         segundo = lista_altura[1]
         terceiro = lista_altura[0]
        
        
    resultado = [f"{segundo:.2f}" , f"{primeiro:.2f}" , f"{terceiro:.2f}"]
        
    return(resultado)

def q5():

    def ler_valores():
        numero = int(input())
        lista = []

        while( numero != 0):
            lista.append(numero)
            numero = int(input())

        return lista

    def processa_lista(valores):
        lista_pares = []
        lista_impares = []
        contador_par = 0
        contador_impar = 0

        for i in valores:
            if(i % 2 == 0):
                contador_par += 1
                if( contador_par > 5):
                    lista_pares[ contador_par - 6] = i
                else:
                    lista_pares.append(i)

            else:
                contador_impar += 1
                if(contador_impar > 5):
                    lista_impares[contador_impar - 6] = i
                else:
                    lista_impares.append(i)

        print(f"Lista de Pares: {lista_pares}")
        print(f"Lista de Impares{lista_impares}")
    processa_lista(ler_valores())
def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)

    


if __name__ == "__main__":
    q5()

