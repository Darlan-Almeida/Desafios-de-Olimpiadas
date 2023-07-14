entrada = "4 7 3 1"
c4, c7, c47, c74 = entrada.split()

num = '4'*int(c4)
num += '7'*int(c7)


def aumenta(x):
    novo = x
    quatro = -1
    saida = ''
    for index, i in enumerate(novo):
        if i == '4':
            quatro = index
    if quatro == -1:
        for i in range(len(novo)+1):
            saida += '4'
    else:
        saida = novo[:quatro]
        saida += '7'
        for i in range(quatro+1, len(novo)):
            saida += '4'
    return saida


v4 = 0
v7 = 0
v47 = 0
v74 = 0

error4 = 0
error7 = 0
error47 = 0
error74 = 0

while True:
    if num.count('4') == int(c4):
        v4 = 1
    elif num.count('4') > int(c4):
        v4 = 0
        error4 = 1
    else:
        v4 = 0
        error4 = 0

    if num.count('7') == int(c7):
        v7 = 1
    elif num.count('7') > int(c7):
        v7 = 0
        error7 = 1
    else:
        v7 = 0
        error7 = 0

    if num.count('47') == int(c47):
        v47 = 1
    elif num.count('47') > int(c47):
        v47 = 0
        error47 = 1
    else:
        v47 = 0
        error47 = 0

    if num.count('74') == int(c74):
        v74 = 1
    elif num.count('74') > int(c74):
        v74 = 0
        error74 = 1
    else:
        v74 = 0
        error74 = 0

    if v4+v7+v47+v74 == 4:
        print(num)
        break
    elif error4+error7+error47+error74 == 4:
        print(-1)
        break
    num = aumenta(num)
