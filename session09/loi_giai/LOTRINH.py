# LOTRINH: n nut giao thong, m duong MOT CHIEU (u -> v). Tim lo trinh di qua it duong nhat tu 1
# den n. Dong 1 in so duong k (khong co thi -1), dong 2 in k+1 nut cua lo trinh. Nhieu lo trinh
# cung ngan nhat thi in lo trinh nao cung duoc. n <= 10^5, m <= 2*10^5.
#   BFS tu 1 nhu bai THANHPHO, nhung do thi CO HUONG: chi them ke[u].append(v).
#   Truy vet: khi tham v tu u, ghi cha[v] = u. Tu n lan cha ve 1 roi DAO NGUOC.
#   Truy vet bang VONG LAP, khong de quy: lo trinh co the dai toi 10^5 nut.
from collections import deque

def main():
    a = list(map(int, open('LOTRINH.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    it = iter(a[2:2 + 2 * m])
    for u, v in zip(it, it):
        ke[u].append(v)                        # mot chieu
    cha = [-1] * (n + 1)                       # cha[v] = dinh lien truoc v tren duong BFS; -1 = chua tham
    cha[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        if u == n:
            break
        for v in ke[u]:
            if cha[v] < 0:
                cha[v] = u
                q.append(v)
    if cha[n] < 0:
        res = '-1\n'
    else:
        duong = []
        v = n
        while v != 0:                          # 1 co cha = 0 nen vong lap dung sau khi them 1
            duong.append(v)
            v = cha[v]
        duong.reverse()
        res = f'{len(duong) - 1}\n' + ' '.join(map(str, duong)) + '\n'
    with open('LOTRINH.OUT', 'w') as f:
        f.write(res)

main()
