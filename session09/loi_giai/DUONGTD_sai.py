# DUONGTD - SAI: BFS tu 1 (khoang cach TU DAU), roi tham lam di xuoi chon dinh ke nho nhat co
# d1[v] = d1[u] + 1. Dinh do co the la ngo cut hoac khong nam tren duong ngan nhat toi n
# -> duong qua dai hoac khong toi n. Phai biet khoang cach DEN DICH (xem DUONGTD.py).
from collections import deque

def main():
    a = list(map(int, open('DUONGTD.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[2 + 2 * i], a[3 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    d1 = [-1] * (n + 1)
    d1[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in ke[u]:
            if d1[v] < 0:
                d1[v] = d1[u] + 1; q.append(v)
    if d1[n] < 0:
        res = '-1\n'
    else:
        duong = [1]
        u = 1
        while u != n:
            ung_vien = [v for v in ke[u] if d1[v] == d1[u] + 1]
            if not ung_vien:                   # ngo cut: dung luon
                break
            u = min(ung_vien)
            duong.append(u)
        res = f'{d1[n]}\n' + ' '.join(map(str, duong)) + '\n'
    with open('DUONGTD.OUT', 'w') as f:
        f.write(res)

main()
