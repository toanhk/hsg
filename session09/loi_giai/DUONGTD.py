# DUONGTD: do thi VO HUONG n dinh, m canh. In duong di it canh nhat tu 1 den n; neu nhieu duong
# cung it canh nhat, in duong co day dinh NHO NHAT theo thu tu tu dien. Dong 1: so canh k
# (khong co duong thi -1), dong 2: k+1 dinh. n <= 10^5, m <= 2*10^5.
# Y chinh (giong bai VANG buoi 8): muon chon dinh tiep theo "nho nhat ma VAN toi uu" thi phai biet
# khoang cach tu moi dinh DEN DICH. Nen BFS tu n, roi di XUOI tu 1:
#   d[v] = so canh it nhat tu v den n (BFS bat dau tu n)
#   Dang o u: dinh tiep theo phai co d[v] = d[u] - 1; chon v NHO NHAT trong cac dinh do.
#   Chon nho nhat o moi buoc (tham lam) la dung vi so sanh tu dien quyet dinh o vi tri khac dau tien.
# BFS O(n + m), di xuoi duyet ke cua cac dinh tren duong: tong <= 2m. ~0,3 giay.
from collections import deque

def main():
    a = list(map(int, open('DUONGTD.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    it = iter(a[2:2 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v); ke[v].append(u)
    d = [-1] * (n + 1)
    d[n] = 0
    q = deque([n])
    while q:
        u = q.popleft()
        du = d[u] + 1
        for v in ke[u]:
            if d[v] < 0:
                d[v] = du; q.append(v)
    if d[1] < 0:
        res = '-1\n'
    else:
        duong = [1]
        u = 1
        while u != n:
            can = d[u] - 1
            u = min(v for v in ke[u] if d[v] == can)
            duong.append(u)
        res = f'{d[1]}\n' + ' '.join(map(str, duong)) + '\n'
    with open('DUONGTD.OUT', 'w') as f:
        f.write(res)

main()
