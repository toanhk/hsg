# CUUHOA - BFS nhieu nguon DUNG thuat toan nhung viet "ngay tho": toa do (i, j), deque cac tuple,
# kiem tra bien 4 lan moi o, mang khoang cach 2 chieu. Dung, nhung voi 10^6 o mat ~1 giay tren may
# cloud -> co the qua gio tren may phong. De chua: so sanh voi CUUHOA.py (ma hoa o + vien tuong + theo lop).
from collections import deque

def main():
    data = open('CUUHOA.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = data[2:2 + m]
    d = [[-1] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 84:                      # 'T'
                d[i][j] = 0; q.append((i, j))
    while q:
        i, j = q.popleft()
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n and g[x][y] != 35 and d[x][y] < 0:
                d[x][y] = d[i][j] + 1; q.append((x, y))
    khong = tong = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 72:                      # 'H'
                if d[i][j] < 0: khong += 1
                else: tong += d[i][j]
    with open('CUUHOA.OUT', 'w') as f:
        f.write(f'{khong} {tong}\n')

main()
