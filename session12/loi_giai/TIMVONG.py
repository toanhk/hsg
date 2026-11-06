# TIMVONG: do thi CO HUONG n dinh, m cung. Neu co chu trinh: in k roi k dinh v1..vk voi
# v1->v2->...->vk->v1 deu la cung (nhieu dap an). Khong co: in -1. n, m <= 2*10^5
# Cach 1 (file nay): Kahn + di nguoc.
#   - Chay Kahn; dinh nao con deg > 0 thi KHONG duoc lay ra -> no co mot cung VAO tu mot dinh
#     cung khong duoc lay ra (neu moi dinh truoc no deu da lay ra thi deg da ve 0).
#   - Ghi truoc[v] = mot dinh u CON LAI co cung u -> v (quet lai danh sach cung mot lan).
#   - Tu mot dinh con lai, di NGUOC theo truoc[]. Luon di tiep duoc, so dinh huu han -> chac chan
#     quay lai dinh da qua: doan tu lan gap dau den nay la chu trinh (dang bi dao chieu).
# Cach 2: DFS 3 mau bang ngan xep (TIMVONG_dfs.py).  O(n + m)
def main():
    data = open('TIMVONG.INP', 'rb').read().split()
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
            if deg[u] and deg[v]:                # ca hai dau deu con lai sau Kahn
                truoc[v] = u
        x = 1
        while deg[x] == 0:                       # mot dinh con lai bat ky
            x += 1
        vt = [-1] * (n + 1)                      # vt[v] = buoc thu may da di qua v
        duong = []
        while vt[x] < 0:
            vt[x] = len(duong); duong.append(x)
            x = truoc[x]
        ct = duong[vt[x]:]
        ct.reverse()                             # di nguoc nen dao lai cho dung chieu cung
        out = f'{len(ct)}\n' + ' '.join(map(str, ct)) + '\n'
    with open('TIMVONG.OUT', 'w') as f:
        f.write(out)

main()
