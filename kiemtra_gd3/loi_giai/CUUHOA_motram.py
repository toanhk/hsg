# CUUHOA - ban trung gian: BFS RIENG tu TUNG tram (deque, ma hoa o), lay min khoang cach cho moi o.
# O(so tram * m * n): dung cho subtask 2 (chi 1 tram), qua thoi gian khi co nhieu tram (subtask 3).
from collections import deque

def main():
    data = open('CUUHOA.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    cam = bytearray(b'\x01') * (W * (m + 2))
    tram, nha = [], []
    for i in range(m):
        r = data[2 + i]
        for j in range(n):
            c = r[j]; u = (i + 1) * W + j + 1
            if c != 35:                                 # khong phai '#'
                cam[u] = 0
                if c == 84: tram.append(u)              # 'T'
                elif c == 72: nha.append(u)             # 'H'
    INF = 10**9
    best = [INF] * len(cam)
    for s in tram:
        d = [-1] * len(cam)
        d[s] = 0; q = deque([s])
        while q:
            u = q.popleft(); du = d[u] + 1
            for v in (u - W, u + W, u - 1, u + 1):
                if not cam[v] and d[v] < 0:
                    d[v] = du; q.append(v)
        for u in nha:
            if 0 <= d[u] < best[u]:
                best[u] = d[u]
    khong = sum(1 for u in nha if best[u] == INF)
    tong = sum(best[u] for u in nha if best[u] < INF)
    with open('CUUHOA.OUT', 'w') as f:
        f.write(f'{khong} {tong}\n')

main()
