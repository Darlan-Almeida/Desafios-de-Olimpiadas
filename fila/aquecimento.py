from collections import deque
import heapq

def primeiros_passos():
    fila = deque()

    while True:
        comand, num = input().split()
        if comand == 'ENQUEUE':
            fila.append(int(num))
        elif comand == 'DEQUEUE':
            if fila:
                fila.popleft()
        else:
            print(" ".join(map(str , fila))) 
            break


def fila_prioridade():
    fila = []
    
    n = int(input())

    while n > 0:
        n -= 1

        id , prioridade = map(int , input().split())
        heapq.heappush(fila , (prioridade , id))

    while fila:
        prioridade , id = heapq.heappop(fila)
        print(id)

fila_prioridade()