# GIAMSAT - vet can (n <= 15): thu moi tap tram lap camera (2^n), kiem tra moi tram duoc giam sat.
def main():
    data = open('GIAMSAT.INP', 'rb').read().split()
    n = int(data[0])
    c = list(map(int, data[1:1 + n]))
    ke = [1 << i for i in range(n)]             # ke[i] = tap {i} hop cac tram noi voi i
    p = 1 + n
    for _ in range(n - 1):
        u, v = int(data[p]) - 1, int(data[p + 1]) - 1; p += 2
        ke[u] |= 1 << v; ke[v] |= 1 << u
    full = (1 << n) - 1
    best = None
    for S in range(1 << n):
        phu = 0; t = 0
        for i in range(n):
            if S >> i & 1:
                phu |= ke[i]; t += c[i]
        if phu == full and (best is None or t < best):
            best = t
    with open('GIAMSAT.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
