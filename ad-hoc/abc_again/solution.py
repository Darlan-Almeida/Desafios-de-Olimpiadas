qtd = input().split()
string = input()
l_string = [s for s in string]

ocorrencia = 0
for i in range(0 , len(string)):
    if i+2 < len(string) and string[i] == 'A' and string[i+1] == 'B' and string[i+2] == 'C':
        ocorrencia += 1

contador = 0
logs = []
while contador < int(qtd[1]):
    query = input().split()
    if l_string[int(query[0])-1] != query[1]:
        if int(query[0])+1 < len(l_string) and query[1] == 'A' and l_string[int(query[0])] == 'B' and l_string[int(query[0])+1] == 'C':
            ocorrencia += 1
        if int(query[0])-2 >= 0 and int(query[0]) < len(l_string) and query[1] == 'B' and l_string[int(query[0])-2] == 'A' and l_string[int(query[0])] == 'C':
            ocorrencia += 1
        if int(query[0])-3 >= 0 and int(query[0])-1 < len(l_string) and query[1] == 'C' and l_string[int(query[0])-2] == 'B' and l_string[int(query[0])-3] == 'A':
            ocorrencia += 1

        if int(query[0])+1 < len(l_string) and query[1] != 'A' and l_string[int(query[0])-1]  == 'A' and l_string[int(query[0])] == 'B' and l_string[int(query[0])+1] == 'C':
            ocorrencia -= 1

        if int(query[0])-2 >= 0 and int(query[0]) < len(l_string) and query[1] != 'B' and l_string[int(query[0])-1]  == 'B' and l_string[int(query[0])-2] == 'A' and l_string[int(query[0])] == 'C':
            ocorrencia -= 1

        if int(query[0])-3 >= 0 and query[1] != 'C' and l_string[int(query[0])-1]  == 'C' and l_string[int(query[0])-3] == 'A' and l_string[int(query[0])-2] == 'B':
            ocorrencia -= 1
    

        l_string[int(query[0]) - 1] = query[1]

    logs.append(ocorrencia)
    contador += 1

for i in logs:
    print(i)