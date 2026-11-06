# CHUTRINH - ban SAI de chua: sau Kahn di TOI (theo cung ra) thay vi di NGUOC.
# Sai vi dinh nam SAU mot chu trinh cung con deg > 0 nhung co the khong co cung ra nao toi dinh con lai
# (vi du trong de: dinh 5 sau vong 2 -> 3 -> 4). Khi do truoc[x] = 0 va vong lap di vao dinh 0 -> in sai.
def main():
    data = open('CHUTRINH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    eu = list(map(int, data[2:2 + 2 * m:2]))    # dau cung
    ev = list(map(int, data[3:3 + 2 * m:2]))    # cuoi cung
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for u, v in zip(eu, ev):
        adj[u].append(v)
        deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    if len(q) == n:
        out = '-1\n'
    else:
        truoc = [0] * (n + 1)
        for u, v in zip(eu, ev):
            if deg[u] and deg[v]:
                truoc[u] = v                     # SAI: ghi dinh KE TIEP, di toi
        x = 1
        while deg[x] == 0:                       # mot dinh con lai bat ky
            x += 1
        vt = [-1] * (n + 1)                      # vt[v] = buoc thu may da di qua v
        duong = []
        while vt[x] < 0:
            vt[x] = len(duong); duong.append(x)
            x = truoc[x]
        ct = duong[vt[x]:]
                             # di nguoc nen dao lai cho dung chieu cung
        out = f'{len(ct)}\n' + ' '.join(map(str, ct)) + '\n'
    with open('CHUTRINH.OUT', 'w') as f:
        f.write(out)

main()
