# CATCANH: cay n thanh pho, thanh pho i co dan so a[i]. Cat dung MOT con duong (canh) de chia thanh hai vung;
# tim chenh lech dan so |S1 - S2| nho nhat. n <= 2*10^5, 1 <= a[i] <= 10^9, n >= 2.
# Goc 1. Cat canh (cha[v], v) thi mot vung la cay con v: S1 = s[v] (tong dan so cay con v), S2 = S - s[v].
#   s[v] tinh nhu kich thuoc cay con (CAYCON) nhung cong a[] thay vi 1 -> duyet nguoc thu tu BFS.
#   Dap an = min_{v != 1} |S - 2*s[v]|. O(n).
def main():
    data = open('CATCANH.INP', 'rb').read().split()
    n = int(data[0])
    s = [0] + list(map(int, data[1:n + 1]))   # s[u] luc dau = a[u], sau duyet nguoc = tong cay con u
    adj = [[] for _ in range(n + 1)]
    it = map(int, data[n + 1:3 * n - 1])
    for u, v in zip(it, it):
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1); par[1] = -1
    order = [1]
    for u in order:
        pu = par[u]
        for v in adj[u]:
            if v != pu:
                par[v] = u; order.append(v)
    for u in reversed(order):
        p = par[u]
        if p > 0:
            s[p] += s[u]
    S = s[1]
    best = min(abs(S - 2 * s[v]) for v in range(2, n + 1))
    with open('CATCANH.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
