from collections import deque

t = int(input())
fila = deque()
while t > 0:
    result = []
    t -= 1
    n = int(input())
    while n > 0:
        n -= 1
        i , l = map(int , input().split())
        fila.append((i , l))

        z = 0
    while fila:
        i , l = fila.popleft()
        if l >= z:
            if i > z:
                z = i
            result.append(str(z))
            z += 1
        else:
            result.append('0')
        
    
    print(" ".join(result))


