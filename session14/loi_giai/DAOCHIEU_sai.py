# DAOCHIEU - BAN SAI de chua bai: BFS 0-1 nhung DANH DAU "da tham" ngay khi dua vao deque (thoi quen
# tu BFS thuong). Mot dinh v duoc dua vao qua canh 1 (d = 1) se bi khoa, sau do du co duong 0 toi v
# cung khong sua duoc nua. Test bat loi: 1 -> 2 la canh nguoc (ton 1) nhung con duong 1 -> 3 -> 2 ton 0.
from collections import deque

def main():
    data = open('DAOCHIEU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append((v, 0)); adj[v].append((u, 1))
    d = [-1] * (n + 1); d[1] = 0
    dq = deque([1])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if d[v] == -1:                 # SAI: lan dau gap la chot luon
                d[v] = d[u] + w
                if w:
                    dq.append(v)
                else:
                    dq.appendleft(v)
    with open('DAOCHIEU.OUT', 'w') as f:
        f.write(str(d[n]) + '\n')

main()
