"""tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def binary_search(v , u , left , right):
    if left > right:
        return 0

    midlle = (left + right) // 2

    if v[midlle] == u:
        qtd = 1
        pos = midlle
        while pos > 0 and v[pos-1] == u:
            pos -= 1
            qtd += 1
        
        pos = midlle
        while pos+1 < len(v) and v[pos+1] == u:
            pos += 1
            qtd += 1
        
        return qtd

    if v[midlle] > u:
        return binary_search(v , u , left , midlle-1)
    else:
        return binary_search(v , u , midlle+1 , right) 

qtd = 0
for i in range(tam1):
    u = l1[i]
    qtd += binary_search(l2 , u , 0 , tam2-1)

print(qtd)"""


"""
tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def binary_search(v , u , left , right ):
    if left > right:
        return 0

    midlle = (left + right) // 2

    if v[midlle] == u:
        r = midlle - 1 if midlle - 1 > 0 else -1
        l = midlle + 1 if midlle + 1 < len(v) else len(v)
        binary_search(v , u , 0 , r) + binary_search(v, u , l, len(v) - 1)
        return 1
    
    if v[midlle] > u:
        return binary_search(v , u , left , midlle-1)
    else:
        return binary_search(v , u , midlle+1 , right) 
qtd = 0
for i in range(tam1):
    u = l1[i]
    qtd += binary_search(l2 , u , 0 , tam2-1 )

print(qtd)

"""


tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def bs_left(v , u , left , right , f):
    if left > right:
        return f
       
    midlle = (left + right) // 2
   
    if v[midlle] == u:
        return bs_left(v , u , left, midlle-1 , midlle)
   
    if v[midlle] > u:
        return bs_left(v , u , left , midlle-1 , f)
   
    return bs_left(v , u , midlle+1 , right , f)
   
   
def bs_right(v , u , left , right , f):
    if left > right:
        return f
       
    midlle = (left + right) // 2
   
    if v[midlle] == u:
        return bs_right(v , u , midlle+1 , right , midlle)
   
    if v[midlle] > u:
        return bs_right(v , u , left , midlle-1 , f)
   
    return bs_right(v , u , midlle+1 , right , f)


qtd = 0
for i in range(tam1):
    elemento = l1[i]
    l = bs_left(l2 , elemento , 0 , len(l2)-1 , -1)
    r = bs_right(l2 , elemento ,0 , len(l2)-1 , -1)

 
    if l == -1 and r == -1:
        qtd += 0
    elif (l == -1 and r != -1) or (l != -1 and r == -1):
        qtd += 1
    else:
        qtd += (r - l + 1)

print(qtd)