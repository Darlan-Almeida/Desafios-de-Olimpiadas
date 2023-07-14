t = "HoUse"

u = 0
l = 0

for i in t:
    if i == i.upper():
        u+=1
    else:
        l+=1

if u > l:
    print(t.upper())
else:
    print(t.lower())