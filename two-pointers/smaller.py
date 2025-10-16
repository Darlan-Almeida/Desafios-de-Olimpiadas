def binary_search_smaller(v , u , left , right):
    if left > right:
        return left
    
    midlle = (left + right) // 2

    if v[midlle] > u:
        return binary_search_smaller(v , u , left , midlle-1)
    else:
        return binary_search_smaller(v , u , midlle+1 , right)



tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
result = []

for i in range(len(l2)):
    pos = (binary_search_smaller(l1 , l2[i] , 0 , len(l1)-1))

    while pos-1 >= 0 and l1[pos-1] == l2[i]:
        pos-=1

    result.append(str(pos))
print(" ".join(result))
