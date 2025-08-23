qtd = input().split()
elementos = input().split()

z = 0
u = 0

for i in elementos:
    if i == '0':
        z += 1
    elif i == '1':
        u += 1

contador = 0
results = []
while contador < int(qtd[1]):
    comand = input().split()
    pos = int(comand[1])
    if comand[0] == '2':
        if pos <= u:
            results.append(1)
        else:
            results.append(0)
    else:
        if elementos[pos-1] == '1':
            elementos[pos-1] = '0'
            u -= 1
            z += 1
        else:
            elementos[pos-1] = '1'
            u += 1
            z -= 1
    contador += 1

for i in results:
    print(i)