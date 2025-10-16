import math


tam , lim = map(int , input().split())
nums = list(map(int , input().split()))


if lim in nums:
    for i in range(tam):
        if nums[i] == lim:
            print(i+1 , 1)
            break
elif len(nums) == 1:
    print(1 , math.ceil(lim / nums[0]))


else:
    i = 0
    j = 1
    music = 2**64 - 1
    i_menor = None
    fell = nums[i]
    looped = True
    while i < tam or music == 2**64 - 1: 
        if j % tam == i and looped and fell > 0:
            looped = False
            loops = lim // fell
            qtd_music = (qtd_music) * loops
            fell = fell * loops
            while fell < lim:
                qtd_music += 1
                fell += nums[j % tam]
                j += 1
            j = (qtd_music - i) - 1
        
        else:
            fell += nums[j % tam]
            qtd_music = abs(i - j) + 1

            
        if fell >= lim:
            if qtd_music < music:
                music = qtd_music
                i_menor = i + 1
            fell -= nums[i]
            fell -= nums[j % tam]
            i += 1
        else:
            j += 1

    print(i_menor , music)   


