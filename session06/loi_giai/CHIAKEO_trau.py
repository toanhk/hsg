# CHIAKEO - vet can: thu moi cach chia (bitmask). Chi qua subtask 1 (n <= 20)
def main():
    data = open('CHIAKEO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tong = sum(a)
    best = tong
    for mask in range(1 << n):
        t = 0
        for i in range(n):
            if mask >> i & 1:
                t += a[i]
        best = min(best, abs(tong - 2 * t))
    with open('CHIAKEO.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
