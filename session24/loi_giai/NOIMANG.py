# NOIMANG (de khoi dong buoi 24, bai 2) - DSU (buoi 15)
# n may tinh, m day cap (co the trung, co the noi may voi chinh no). In: so day it nhat can them de moi may
# lien thong (= so cum - 1) va so may cua cum lon nhat HIEN TAI. n, m <= 2*10^5.
# DSU nen nua duong + hop theo kich thuoc, find khong de quy. Do ~0,25 s.
def main():
    data = open('NOIMANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    par = list(range(n + 1))
    sz = [1] * (n + 1)

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    cum = n
    it = iter(map(int, data[2:2 + 2 * m]))
    for u, v in zip(it, it):
        a, b = find(u), find(v)
        if a != b:
            if sz[a] < sz[b]:
                a, b = b, a
            par[b] = a; sz[a] += sz[b]; cum -= 1
    lon = max(sz[x] for x in range(1, n + 1) if par[x] == x)
    with open('NOIMANG.OUT', 'w') as f:
        f.write(f'{cum - 1}\n{lon}\n')

main()
