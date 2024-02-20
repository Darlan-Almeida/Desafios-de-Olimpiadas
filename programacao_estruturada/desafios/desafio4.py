#referencia: https://www.thehuxley.com/problem/2842?quizId=4323
def q1():
    n = int(input(''))
    lista_multiplos = []
    divisores = 0

    for i in range(1 , n+1):
        
        if(n % i == 0):
            lista_multiplos.append(i)

    for i in lista_multiplos:
        if(i % 3 == 0):
            divisores += 1
    
    if(divisores > 0):
        print("Quantidade de divisores divisiveis por 3: {0}".format(divisores))
    else:
        print('O número não possui divisores multiplos de 3')
        

#referencia: https://www.thehuxley.com/problem/406?quizId=4323
def q2():
    n1 = int(input(''))
    n2 = int(input(''))
    resultado = 0

    if(n1 > n2):
        if(n2 >= 0):
            for i in range(n2 , n1 + 1):
                resultado += i
        else:
            for i in range(n1 + 1):
                resultado += i
        
    if(n2 > n1):
        if(n1 >= 0):
            for i in range(n1 , n2 + 1):
                resultado += i
        else:
            for i in range(n2 + 1):
                resultado += i


    print(resultado)

def q3():
    servidores = float(input(''))
    unidades = float(input(''))
    armazenamento = float(input(''))
    dados = float(input(''))

    total = (servidores * 500) + (unidades * 100) + (armazenamento *0.10) + (dados * 0.05)

    if(total > 10000):
        print("O custo total mensal está acima do limite.")

    else:
        print(f"O custo total mensal estimado para a infraestrutura é de R$ {total:>.2f}." )

#referencia: https://www.thehuxley.com/problem/1089
def q4():
    n = int(input(''))
    zero = 0
    soma = 0
    lista = []
    if(n > 0):
        for i in range(1 , n+1):
            denominador = i * 3
            soma += i/denominador
            lista.append(f"{i}/{denominador}")
        for index,i in enumerate(lista):
            if(index != len(lista)-1):
                print(f"{i} + " , end='')
                    
            else:
                print(i)
        print(f"{soma:.2f}")
    else:
        print(f"{zero:.1f}")

