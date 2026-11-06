# CONGVIEC: n cong viec, viec i lam mat t[i] ngay; m rang buoc "viec u xong thi viec v moi duoc bat dau".
# Co du tho de lam song song moi viec. In T = so ngay it nhat de xong het, va so viec GANG (tre 1 ngay la
# T tang). Neu rang buoc tao vong: in -1.  n, m <= 10^5, t[i] <= 10^6
# (Gioi han 10^5 chu khong 2*10^5: bai can HAI lan duyet do thi, voi 2*10^5 mat ~0,55 giay.)
# Hai lan QHD tren thu tu to-po (phuong phap duong gang - CPM):
#   Xuoi : xong_som[v] = t[v] + max xong_som[u] (u -> v), mac dinh t[v]. T = max xong_som.
#   Nguoc: xong_muon[u] = min (xong_muon[v] - t[v]) voi u -> v, mac dinh T (viec khong co viec sau).
#   Viec v la gang  <=>  xong_som[v] == xong_muon[v]  (khong co "do tre" nao), tuong duong
#   bat dau som nhat == bat dau muon nhat. min(map(...)) day vong trong xuong C cho nhanh.
# Duyet nguoc thu tu to-po: moi viec sau v deu da co xong_muon khi xet v.  O(n + m)
from operator import add, eq

def main():
    data = open('CONGVIEC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    t = [0] + [int(x) for x in data[2:2 + n]]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    p = 2 + n
    for i in range(p, p + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    bat_dau = [0] * (n + 1)                   # bat dau som nhat = max xong_som cua viec truoc
    for u in q:
        xu = bat_dau[u] + t[u]
        for v in adj[u]:
            if xu > bat_dau[v]:
                bat_dau[v] = xu
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    if len(q) < n:
        out = '-1\n'
    else:
        som = list(map(add, bat_dau, t))       # xong som nhat cua tung viec
        T = max(som)
        muon_bd = [0] * (n + 1)                # muon_bd[v] = bat dau MUON nhat cua v
        get = muon_bd.__getitem__
        for u in reversed(q):                  # nguoc thu tu to-po: viec sau u da co muon_bd
            xong_muon = min(map(get, adj[u]), default=T)
            muon_bd[u] = xong_muon - t[u]
        gang = sum(map(eq, bat_dau, muon_bd)) - 1   # tru phan tu 0 (luon bang 0 = 0)
        out = f'{T} {gang}\n'
    with open('CONGVIEC.OUT', 'w') as f:
        f.write(out)

main()
