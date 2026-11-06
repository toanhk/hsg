# BIENSO - QUEN chan y >= 0. Khi x = 0, y = x - 1 = -1 va dist[-1] chinh la dist[10^6]:
# Python khong bao loi, dist[10^6] bi gan sai, so -1 con duoc day vao hang doi va sinh tiep
# -2, -3... (dist[-2] = dist[10^6 - 1]). Chi sai khi duong BFS cham toi 0 va B gan 10^6.
from collections import deque

L = 10**6

def main():
    A, B = map(int, open('BIENSO.INP', 'rb').read().split()[:2])
    dist = [-1] * (L + 1)
    dist[A] = 0
    q = deque([A])
    while dist[B] < 0:
        x = q.popleft()
        for y in (x + 1, x - 1, 2 * x):
            if y <= L and dist[y] < 0:         # <- thieu y >= 0
                dist[y] = dist[x] + 1
                q.append(y)
    with open('BIENSO.OUT', 'w') as f:
        f.write(str(dist[B]) + '\n')

main()
