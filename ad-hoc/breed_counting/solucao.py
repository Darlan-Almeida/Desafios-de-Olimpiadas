with open("bcount.in", "r") as f:
    n, q = map(int, f.readline().split())

    h = [0]
    g = [0]
    j = [0]

    while n > 0:
        n -= 1
        raca = int(f.readline())

        if raca == 1:
            h.append(h[-1] + 1)
            j.append(j[-1])
            g.append(g[-1])
        elif raca == 2:
            g.append(g[-1] + 1)
            h.append(h[-1])
            j.append(j[-1])
        else:
            j.append(j[-1]+1)
            g.append(g[-1])
            h.append(h[-1])
with open("bcount.out", "w") as out:
    while q > 0:
        q -= 1
        l , r = map(int , f.readline().split())
        h_count = h[r] - h[l-1]
        g_count = g[r] - g[l-1]
        j_count = j[r] - j[l-1]

        out.write(f"{h_count} {g_count} {j_count}\n")


