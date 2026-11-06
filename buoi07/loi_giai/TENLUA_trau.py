# TENLUA - vet can (n <= 12):
#   (1) thu moi tap con, giu tap khong tang dai nhat
#   (2) thu k = 1, 2, ...: quay lui gan tung qua cho mot trong k he thong (moi he thong nho phat cuoi)
def main():
    data = open('TENLUA.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    c1 = 0
    for mask in range(1, 1 << n):
        t = [h[i] for i in range(n) if mask >> i & 1]
        if len(t) > c1 and all(t[i] >= t[i + 1] for i in range(len(t) - 1)):
            c1 = len(t)

    def gan_duoc(k):
        cuoi = []                           # phat cuoi cua cac he thong da mo
        def thu(i):
            if i == n:
                return True
            for s in range(len(cuoi)):
                if cuoi[s] >= h[i]:
                    cu = cuoi[s]; cuoi[s] = h[i]
                    if thu(i + 1):
                        return True
                    cuoi[s] = cu
            if len(cuoi) < k:               # mo he thong moi
                cuoi.append(h[i])
                if thu(i + 1):
                    return True
                cuoi.pop()
            return False
        return thu(0)

    c2 = 1
    while not gan_duoc(c2):
        c2 += 1
    with open('TENLUA.OUT', 'w') as out:
        out.write(f'{c1}\n{c2}\n')

main()
