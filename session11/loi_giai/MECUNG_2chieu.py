# MECUNG - BFS kieu "sach giao khoa": deque chua tuple (i, j), mang dist 2 chieu, mang dx/dy,
# kiem tra bien moi lan. Dung nhung ~3 lan cham hon MECUNG.py: 1000 x 1000 mat ~0.7 s (sat 1 giay).
from collections import deque

def main():
    data = open('MECUNG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = data[2:2 + m]
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    dist = [[-1] * n for _ in range(m)]
    for i in range(m):
        j = g[i].find(b'S')
        if j >= 0:
            si, sj = i, j
        j = g[i].find(b'E')
        if j >= 0:
            ei, ej = i, j
    dist[si][sj] = 0
    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        if i == ei and j == ej:
            break
        for k in range(4):
            u, v = i + dx[k], j + dy[k]
            if 0 <= u < m and 0 <= v < n and g[u][v] != 35 and dist[u][v] == -1:
                dist[u][v] = dist[i][j] + 1
                q.append((u, v))
    with open('MECUNG.OUT', 'w') as f:
        f.write(str(dist[ei][ej]) + '\n')

main()
