entrada = input()
distintos = set()
for i in entrada:
    distintos.add(i)

if len(distintos) % 2 == 1:
     print('IGNORE HIM!') 
else: 
    print("CHAT WITH HER!")