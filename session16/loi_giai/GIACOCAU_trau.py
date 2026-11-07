# GIACOCAU - vet can (n <= 8, m <= 12): thu moi tap n-1 cau chua du cac cau bat buoc va noi duoc moi xa.
from itertools import combinations

def main():
    data = open('GIACOCAU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[i]), int(data[i + 1]), int(data[i + 2]), int(data[i + 3])) for i in range(2, 2 + 4 * m, 4)]
    can = sum(t for u, v, w, t in canh)
    best = -1
    for tap in combinations(canh, n - 1):
        if sum(e[3] for e in tap) != can:
            continue                           # thieu cau bat buoc
        adj = [[] for _ in range(n + 1)]
        for u, v, w, t in tap:
            adj[u].append(v); adj[v].append(u)
        da = {1}; q = [1]
        for u in q:
            for v in adj[u]:
                if v not in da:
                    da.add(v); q.append(v)
        if len(da) == n:
            best = max(best, sum(e[2] for e in tap))
    with open('GIACOCAU.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
