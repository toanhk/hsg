# TAUHOA - vet can: lap noi long moi tuyen (kieu Bellman-Ford) cho den khi khong con gi thay doi.
# O(n * m), chi cho n, m nho.
def main():
    data = list(map(int, open('TAUHOA.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    tuyen = [tuple(data[2 + 4 * i: 6 + 4 * i]) for i in range(m)]
    INF = float('inf')
    t = [INF] * (n + 1)
    t[1] = 0
    doi = True
    while doi:
        doi = False
        for u, v, c, p in tuyen:
            if t[u] < INF:
                den = -(-t[u] // p) * p + c
                if den < t[v]:
                    t[v] = den
                    doi = True
    with open('TAUHOA.OUT', 'w') as f:
        f.write((str(t[n]) if t[n] < INF else '-1') + '\n')

main()
