saltos = [1 , 2 , 3 , 4 , 5]
x = int(input())

jogadas = 0

i = 1
if(x <= 5):
    print(1)

else:

    while( x > 0):
        valor = saltos[-1]
        if(x >= valor):
            i += 1
            jogadas += 1
            x -= valor
        else:
            saltos.pop(-1)
    print(jogadas)
