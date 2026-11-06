# DOCTHAP - cach 2: TIM KIEM NHI PHAN dap an + BFS. "Chi di cac doan co h <= X, co toi t khong?" la tinh chat
# don dieu theo X (X cang lon cang de). Tim X nho nhat trong danh sach cac h da sap xep.
# O((n + m) log m): ~17 lan BFS tren do thi 2*10^5 canh -> ~1,5 s, QUA GIO voi subtask 3.
# Van dang hoc: ky thuat "nhi phan dap an + kiem tra" dung duoc cho nhieu bai khong co Kruskal.
def di_duoc(n, adj, s, t, X):
    da = [False] * (n + 1)
    da[s] = True; q = [s]
    for u in q:
        for v, h in adj[u]:
            if h <= X and not da[v]:
                da[v] = True; q.append(v)
    return da[t]

def main():
    data = open('DOCTHAP.INP', 'rb').read().split()
    n, m, s, t = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    adj = [[] for _ in range(n + 1)]
    hs = []
    for i in range(4, 4 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); h = int(data[i + 2])
        adj[u].append((v, h)); adj[v].append((u, h)); hs.append(h)
    if s == t:
        kq = 0
    else:
        hs = sorted(set(hs))
        lo, hi = 0, len(hs) - 1
        kq = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if di_duoc(n, adj, s, t, hs[mid]):
                kq = hs[mid]; hi = mid - 1
            else:
                lo = mid + 1
    with open('DOCTHAP.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
