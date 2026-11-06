# ECHNHAY - vet can: quay lui thu moi duong nhay tu hon 1 den hon n, giu duong it ton nhat.
# So duong nhay ~ 2^(n-2) khi k lon: n = 20 -> 2.6*10^5 duong. Chi cho subtask 1 (n <= 20).
def main():
    data = open('ECHNHAY.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    h = list(map(int, data[2:2 + n]))
    tot = float('inf')

    def thu(i, suc):                    # dang dung o hon i (chi so 0), da ton 'suc'
        nonlocal tot
        if i == n - 1:
            tot = min(tot, suc)
            return
        for j in range(i + 1, min(n, i + k + 1)):
            thu(j, suc + abs(h[i] - h[j]))

    thu(0, 0)
    with open('ECHNHAY.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
