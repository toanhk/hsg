# CAYCON - vet can (n <= 1000): tim cha bang BFS, roi voi MOI dinh x di nguoc len goc,
# cong 1 cho moi dinh tren duong (x nam trong cay con cua tat ca to tien cua no). O(n * do sau).
def main():
    data = open('CAYCON.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1)
    da = [False] * (n + 1); da[1] = True
    q = [1]
    for u in q:
        for v in adj[u]:
            if not da[v]:
                da[v] = True; par[v] = u; q.append(v)
    sz = [0] * (n + 1)
    for x in range(1, n + 1):
        y = x
        while y != 0:
            sz[y] += 1
            y = par[y]
    with open('CAYCON.OUT', 'w') as f:
        f.write(' '.join(map(str, sz[1:])) + '\n')

main()
