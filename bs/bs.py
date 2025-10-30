import bisect

# bisect.bisect
def bs(v, x):
    l, r = 0 , len(v)-1
    while l <= r:
        midlle = (l+r) // 2

        if v[midlle] == x:
            return midlle
        elif v[midlle] > x:
            r = midlle - 1
        else:
            l = midlle + 1
    
    return - 1

# bisect.bisect_left
def lower_bound(v, x):
    l, r = 0, len(v)
    while l < r:
        mid = (l + r) // 2
        if v[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l



# bisect.bisect_right
def upper_bound(v , x):
    l , r = 0 , len(v)

    while l < r:
        midlle = (l+r) // 2

        if v[midlle] > x:
            r = midlle
        else:
            l = midlle + 1

    return r

# maior dos menores
def strictly_less(a, x):
    idx = bisect.bisect_left(a, x)
    return idx-1 if idx > 0 else -1

def less_or_equal(a, x):
    idx = bisect.bisect_right(a, x)
    return idx-1 if idx > 0 else -1


a = [1, 3, 3, 5, 7, 9, 11]

assert strictly_less(a, 5) == 2
assert strictly_less(a, 1) == -1
assert strictly_less(a, 12) == len(a) - 1
assert less_or_equal(a, 5) == 3
assert less_or_equal(a, 6) == 3
assert less_or_equal(a, 0) == -1
assert less_or_equal(a, 1) == 0
assert less_or_equal(a, 12) == len(a) - 1
# ===============================
# 🔹 TESTES AUTOMÁTICOS COM ASSERTS
# ===============================

a = [1, 3, 5, 7, 9, 11]

# --- bs ---
assert bs(a, 7) == 3
assert bs(a, 2) == -1
assert bs(a, 10) == -1
assert bs(a, 11) == 5
assert bs(a, 1) == 0

# --- lower_bound ---
a = [1, 3, 3, 5, 7, 9, 11]
assert lower_bound(a, 7) == 4
assert lower_bound(a, 2) == 1
assert lower_bound(a, 10) == 6
assert lower_bound(a, 0) == 0
assert lower_bound(a, 3) == 1
assert lower_bound(a, 4) == 3
assert lower_bound(a, 12) == 7
assert lower_bound(a, 11) == 6
assert lower_bound(a, -5) == 0
assert lower_bound(a, 5) == 3

# --- upper_bound ---
assert upper_bound(a, 7) == 5
assert upper_bound(a, 2) == 1
assert upper_bound(a, 10) == 6
assert upper_bound(a, 0) == 0
assert upper_bound(a, 3) == 3
assert upper_bound(a, 4) == 3
assert upper_bound(a, 12) == 7
assert upper_bound(a, 11) == 7
assert upper_bound(a, -2) == 0
assert upper_bound(a, 5) == 4

# --- Comparação com bisect ---
for x in range(-1, 15):
    assert lower_bound(a, x) == bisect.bisect_left(a, x)
    assert upper_bound(a, x) == bisect.bisect_right(a, x)

print("✅ Todos os testes passaram com sucesso!")