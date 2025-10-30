'''



AC KC QC JC TC 8C 8C 7C 6C 9C 4C 3C 2C AD KD QD   
KH QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S 

Y = 9
2D 9H 

Y = 12
TD 9D 8D 7D 6D 5D 4D 3D

Y = 22


AC KC QC JC TC 9C 8C 7C 6C 5C 4C 3C 2C AD KD QD     


KH QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S  

AH
X = 10 Y = 10

2D
X = 2 Y = 12
TD 9D 8D 7D 6D 5D 4D 3D

JD
X = 10; Y=22

22 posicao = 8H

'''

from collections import deque

t = int(input())
k = int(0)
while t > 0:
    t -= 1
    entrada = input().split()
    cartas = deque()
    mao = deque()
    for i in range(52):
        if i < 27:
            cartas.appendleft(entrada[i])
        else:
            mao.appendleft(entrada[i])

    
    y = 0

    exec = 3
    while exec > 0:
        exec -= 1
        c_monte = cartas.popleft()
        x = 10 if c_monte[0] not in [  '2' ,'3' , '4' , '5' , '6' , '7' , '8' , '9'] else int(c_monte[0])
        y += x

        loops = 10 - x

        while loops > 0 and cartas:
            loops -= 1 
            cartas.popleft()


    result = ''
    while y > 0:
        y -= 1
        if not cartas:
            result = mao.pop()
        else:
            result = cartas.pop()
    
    k += 1
    print(f"Case {k}: {result}")