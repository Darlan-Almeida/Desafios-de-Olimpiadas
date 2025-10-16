def binary_search(v , u , left , right):

    if left > right:
        return -1
    
    pos = int((left + right) / 2)

    if v[pos] == u:
        return pos
    if v[pos] < u:
        return binary_search(v , u , pos+1 , right)
    else:
        return binary_search(v , u , left , pos-1)

a=[1,3,5,8,10]
b=[2,6,7,9,13]


# Merge Duas Listas
c = [None] *10
i = 0
j = 0
while i < len(a) or j < len(b):
    if j == len(b) or i < len(a) and a[i] < b[j]:
       c[i + j] = a[i]
       i += 1
    else:
       c[i + j] = b[j]
       j += 1

print(c)


def binary_search_smaller(v , u , left , right):
    if left > right:
        return left
    
    pos = int((left + right) / 2)
    if v[pos] < u:
        return binary_search_smaller(v , u , pos+1 , right)
    else:
        return binary_search_smaller(v , u , left , pos-1)

def two_pointers_smaller(v , u):
    count = 0
    for i in range(len(v)):
        if v[i] < u:
            count += 1
        else:
            break
    
    return count



for i in range(len(b)):
    elemento = b[i]
    print(binary_search_smaller(a , elemento , 0 , len(a)-1) , elemento)
    print(two_pointers_smaller(a , elemento), elemento)
