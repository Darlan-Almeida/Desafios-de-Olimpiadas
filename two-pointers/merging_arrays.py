tam1, tam2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

i = j = 0
out = []

while j < len(l1) or i < len(l2):
    if j == len(l1) or (i < len(l2) and l2[i] < l1[j]):
        out.append(str(l2[i]))
        i += 1
    else:
        out.append(str(l1[j]))
        j += 1

print(" ".join(out))
