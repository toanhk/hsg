# DUONGTD - cach 2 (cung dung): SAP XEP moi danh sach ke tang dan roi BFS tu 1 ghi cha[] nhu
# bai LOTRINH. Dinh nao duoc phat hien truoc thi cha cua no co duong tu dien nho hon, nen duong
# truy vet cung la duong tu dien nho nhat. Ton them thoi gian sort (~0,1 giay).
from collections import deque

def main():
    a = list(map(int, open('DUONGTD.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    it = iter(a[2:2 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v); ke[v].append(u)
    for x in ke:
        x.sort()
    cha = [-1] * (n + 1)
    cha[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        if u == n:
            break
        for v in ke[u]:
            if cha[v] < 0:
                cha[v] = u; q.append(v)
    if cha[n] < 0:
        res = '-1\n'
    else:
        duong = []
        v = n
        while v:
            duong.append(v); v = cha[v]
        duong.reverse()
        res = f'{len(duong) - 1}\n' + ' '.join(map(str, duong)) + '\n'
    with open('DUONGTD.OUT', 'w') as f:
        f.write(res)

main()
