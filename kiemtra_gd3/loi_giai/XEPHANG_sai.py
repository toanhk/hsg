# XEPHANG - ban SAI de chua: thay hang doi co >= 2 doi la in 0 va dung NGAY, khong chay Kahn den het.
# Sai khi ket qua vua mo ho vua mau thuan: dap an phai la -1 (khong co bang nao) chu khong phai 0.
def main():
    data = open('XEPHANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    out = None
    dau = 0
    while dau < len(q):
        if len(q) - dau > 1:
            out = '0'
            break
        u = q[dau]; dau += 1
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    if out is None:
        out = '-1' if len(q) < n else ' '.join(map(str, q))
    with open('XEPHANG.OUT', 'w') as f:
        f.write(out + '\n')

main()
