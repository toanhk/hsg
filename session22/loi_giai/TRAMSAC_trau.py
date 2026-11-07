# TRAMSAC - vet can (n <= 15): thu moi tap tram duoc sac, kiem tra moi doan giua hai lan sac lien tiep <= L.
def main():
    data = open('TRAMSAC.INP', 'rb').read().split()
    n, L, P = int(data[0]), int(data[1]), int(data[2])
    x = [int(data[3 + 2 * i]) for i in range(n)]
    c = [int(data[4 + 2 * i]) for i in range(n)]
    best = -1
    for mask in range(1 << n):
        cur, tien, ok = 0, 0, True
        for i in range(n):
            if mask >> i & 1:
                if x[i] - cur > L:
                    ok = False; break
                cur = x[i]; tien += c[i]
        if ok and P - cur <= L and (best < 0 or tien < best):
            best = tien
    with open('TRAMSAC.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
