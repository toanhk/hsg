# DOCTHAP - vet can (n <= 8): quay lui moi duong di DON tu s den t (khong lap dinh), lay min cua max h.
def main():
    data = open('DOCTHAP.INP', 'rb').read().split()
    n, m, s, t = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    adj = [[] for _ in range(n + 1)]
    for i in range(4, 4 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); h = int(data[i + 2])
        adj[u].append((v, h)); adj[v].append((u, h))
    best = [-1]
    da = [False] * (n + 1)

    def thu(u, cao):                           # dang o u, doan doc nhat da qua = cao
        if u == t:
            if best[0] < 0 or cao < best[0]:
                best[0] = cao
            return
        for v, h in adj[u]:
            if not da[v]:
                da[v] = True
                thu(v, max(cao, h))
                da[v] = False

    da[s] = True
    thu(s, 0)
    with open('DOCTHAP.OUT', 'w') as f:
        f.write(str(best[0]) + '\n')

main()
