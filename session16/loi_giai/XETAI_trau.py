# XETAI - vet can: moi truy van BFS lai tu s, chi di cau co w >= L. O(q * (n + m)): chi dung cho subtask 1.
def main():
    data = open('XETAI.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    adj = [[] for _ in range(n + 1)]
    for i in range(3, 3 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        adj[u].append((v, w)); adj[v].append((u, w))
    p = 3 + 3 * m
    out = []
    for k in range(q):
        s = int(data[p + 2 * k]); L = int(data[p + 2 * k + 1])
        da = [False] * (n + 1)
        da[s] = True; hd = [s]
        for u in hd:
            for v, w in adj[u]:
                if w >= L and not da[v]:
                    da[v] = True; hd.append(v)
        out.append(str(len(hd)))
    with open('XETAI.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
