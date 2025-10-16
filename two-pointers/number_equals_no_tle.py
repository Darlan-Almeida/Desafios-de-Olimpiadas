tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def binary_search(v , u , left , right , qtd):
    if left > right:
        return 0

    midlle = (left + right) // 2

    if v[midlle] == u:
        return binary_search(v , u , 0 , midlle-1 , 1) + binary_search(v, u , midlle + 1, len(v) - 1)

    if v[midlle] > u:
        return binary_search(v , u , left , midlle-1)
    else:
        return binary_search(v , u , midlle+1 , right) 

qtd = 0
for i in range(tam1):
    u = l1[i]
    qtd += binary_search(l2 , u , 0 , tam2-1 , 0)

print(qtd)