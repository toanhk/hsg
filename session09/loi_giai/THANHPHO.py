# THANHPHO: n thanh pho, m con duong HAI CHIEU. Tim so con duong it nhat phai di tu s den t;
# khong di duoc thi in -1. n, m <= 2*10^5 (co the co canh lap, khong co khuyen).
# Mo hinh: dinh = thanh pho, canh = con duong, "it con duong nhat" = it canh nhat -> BFS.
#   dist[v] = so canh it nhat tu s den v, -1 = chua tham
#   Lay u ra khoi hang doi, moi v ke u chua tham: dist[v] = dist[u] + 1, day v vao cuoi hang doi
#   Danh dau NGAY KHI DAY VAO (khong doi luc lay ra) de moi dinh vao hang doi dung mot lan
# Do phuc tap O(n + m): ~0,3 giay voi n = m = 2*10^5 (xem do_bfs.py).
from collections import deque

def main():
    a = list(map(int, open('THANHPHO.INP', 'rb').read().split()))
    n, m, s, t = a[0], a[1], a[2], a[3]
    ke = [[] for _ in range(n + 1)]            # KHONG viet [[]] * (n + 1): cac dinh dung chung 1 list
    it = iter(a[4:4 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v)
        ke[v].append(u)                        # hai chieu: them ca hai phia
    dist = [-1] * (n + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t:                             # lay t ra la xong: dist[t] da toi uu
            break
        du = dist[u] + 1
        for v in ke[u]:
            if dist[v] < 0:
                dist[v] = du
                q.append(v)
    with open('THANHPHO.OUT', 'w') as f:
        f.write(str(dist[t]) + '\n')

main()
