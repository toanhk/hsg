# CUUHOA - vet can: BFS tu TUNG NHA (toa do (i, j), kiem tra bien), dung khi gap tram dau tien.
# O(so nha * m * n): chi dung cho subtask 1 (m, n <= 30).
from collections import deque

def main():
    data = open('CUUHOA.INP').read().split()
    m, n = int(data[0]), int(data[1])
    g = data[2:2 + m]
    khong = tong = 0
    for si in range(m):
        for sj in range(n):
            if g[si][sj] != 'H':
                continue
            d = {(si, sj): 0}; q = deque([(si, sj)]); kq = -1
            while q:
                i, j = q.popleft()
                if g[i][j] == 'T':
                    kq = d[(i, j)]; break
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and g[x][y] != '#' and (x, y) not in d:
                        d[(x, y)] = d[(i, j)] + 1; q.append((x, y))
            if kq < 0: khong += 1
            else: tong += kq
    with open('CUUHOA.OUT', 'w') as f:
        f.write(f'{khong} {tong}\n')

main()
