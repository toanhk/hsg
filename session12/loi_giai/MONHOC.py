# MONHOC: n mon hoc, m quan he "mon u phai hoc truoc mon v". In mot thu tu hoc ca n mon
# thoa moi quan he (nhieu dap an -> in thu tu nao cung duoc), hoac -1 neu khong the. n, m <= 2*10^5
# Thuat toan Kahn: bac vao deg[v] = so mon tien quyet CHUA hoc cua v.
#   - Cho moi mon co deg = 0 vao hang doi (hoc duoc ngay).
#   - Lay u ra, hoc u; moi canh u -> v: deg[v] -= 1, neu ve 0 thi v vao hang doi.
#   - Hoc du n mon -> in thu tu; thieu -> cac mon con lai nam tren (hoac sau) mot chu trinh -> -1.
# O(n + m). Dung list q lam hang doi: "for u in q" van chay tiep khi q.append them phan tu.
def main():
    data = open('MONHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v)
        deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:                        # q vua la hang doi vua la thu tu to-po
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('MONHOC.OUT', 'w') as f:
        if len(q) < n:
            f.write('-1\n')
        else:
            f.write(' '.join(map(str, q)) + '\n')

main()
