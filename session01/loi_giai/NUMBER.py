# NUMBER - HSG 12 Ninh Binh 2019-2020, bai 1
# Dem X trong [P, Q] sao cho X va so dao nguoc cua X deu nguyen to. Q <= 10^4.
def main():
    data = open('NUMBER.INP', 'rb').read().split()
    p, q = int(data[0]), int(data[1])

    # Sang Eratosthenes den 10^4 (so dao cua so <= 10^4 cung <= 9999)
    N = 10**4
    nt = [True] * (N + 1)
    nt[0] = nt[1] = False
    for i in range(2, int(N**0.5) + 1):
        if nt[i]:
            for j in range(i * i, N + 1, i):
                nt[j] = False

    dem = 0
    for x in range(p, q + 1):
        if nt[x] and nt[int(str(x)[::-1])]:   # dao so bang xau
            dem += 1

    with open('NUMBER.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
