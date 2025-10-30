nums = list(map(int , input().split()))

maior , menor = max(nums) , min(nums)


if menor > 1:
    print(maior * (menor//2) + (maior//2) * (menor % 2))
else:
    print(maior // 2)