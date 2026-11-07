# TIENQUYET - vet can (n <= 15): thu moi tap dung k mon, kiem tra moi mon chon deu co tien quyet duoc chon.
def main():
    data = open('TIENQUYET.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    p = [int(data[2 * i]) - 1 for i in range(1, n + 1)]     # -1: khong co tien quyet
    c = [int(data[2 * i + 1]) for i in range(1, n + 1)]
    best = None
    for mask in range(1 << n):
        if bin(mask).count('1') != k:
            continue
        ok = all(p[i] < 0 or mask >> p[i] & 1 for i in range(n) if mask >> i & 1)
        if ok:
            t = sum(c[i] for i in range(n) if mask >> i & 1)
            if best is None or t > best:
                best = t
    with open('TIENQUYET.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
