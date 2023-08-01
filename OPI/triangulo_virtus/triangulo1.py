import math

#  N * (N - 1) * (N - 2) / 6


n = int(input())

colinear = 0
cordenadas = []
lista_cordenadas = []
qtd = 0
cordenadax = []

cordenaday = []
for i in range(n):
    cordenada = input().split()
    cordenadas.append(cordenada)

for i in cordenadas:
    for j in i:
        lista_cordenadas.append(j)


for index,i in enumerate(lista_cordenadas):
    if(index % 2 != 0):
        cordenaday.append(i)

    else:
        cordenadax.append(i)


for item in set(cordenadax):
    colinear += math.floor(cordenadax.count( item)/ 3)


for item in set(cordenaday):
    colinear += math.floor(cordenaday.count( item)/ 3)

for i in range(len(cordenadax)):
    if(cordenadax[i] == cordenaday[i]):
        qtd += 1

colinear += math.floor(qtd / 3)


def formula_triangulos( n ,colineares ):
    resultado = round((n * (n - 1) * (n - 2) / 6) - colineares)
    return resultado


print(formula_triangulos(n , colinear))
