from collections import deque

t = int(input())
for case in range(1, t + 1):
    entrada = input().split()
    cartas = deque(entrada[:27])   # 27 de baixo
    mao = deque(entrada[27:])      # 25 do topo
    y = 0

    print(cartas , len(cartas))
    print(mao, len(mao))
    for _ in range(3):
        c_monte = cartas.pop()  # topo é o fim da deque
        x = int(c_monte[0]) if c_monte[0] in '23456789' else 10
        y += x
        for _ in range(10 - x):
            cartas.pop()

    # devolve as 25 cartas da mão sobre o monte
    while mao:
        cartas.append(mao.pop())

    # y-ésima carta a partir da base
    result = cartas[y - 1]
    print(f"Case {case}: {result}")
