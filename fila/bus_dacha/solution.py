from collections import deque
n , m = map(int , input().split())
g = list(map(int , input().split()))

fila = deque(g)

bus = 0
while fila:
    x = fila.popleft()
    if x > m:
        fila.appendleft(x - m)
        bus += 1
    elif x < m:
        espaco = m - x
        while fila:
            y = fila.popleft()
            if espaco < y:
                fila.appendleft(y)                
                break
            espaco -= y
        bus += 1
    else:
        bus += 1



print(bus)