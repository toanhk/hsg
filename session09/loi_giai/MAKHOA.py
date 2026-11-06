# MAKHOA: O khoa co n banh xe so (1 <= n <= 5), moi banh mang chu so 0..9. Moi buoc xoay MOT banh
# len hoac xuong 1 nac (9 len thanh 0, 0 xuong thanh 9). Khoa dang o ma S, can mo ma T, nhung co
# k ma cam (khoa ket neu xoay toi). In so buoc it nhat, khong duoc thi -1. S khong bi cam.
# Mo hinh: dinh = ma (so nguyen 0..10^n - 1), canh = xoay 1 banh -> moi dinh co 2n canh. BFS tu S.
#   Chu so o vi tri p = 10^i:  c = x // p % 10
#   Xoay len : c < 9 -> x + p ; c = 9 -> x - 9p.   Xoay xuong: c > 0 -> x - p ; c = 0 -> x + 9p
#   Ma cam: danh dau dist = -2 truoc khi BFS -> khong bao gio duoc tham (chung mot lenh if).
# 10^5 dinh x 10 canh = 10^6 lan xet canh: ~0,4 giay.
from collections import deque

def main():
    data = open('MAKHOA.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    S, T = int(data[2]), int(data[3])           # int(b'0012') = 12: so 0 dau khong anh huong
    N = 10**n
    dist = [-1] * N
    for i in range(4, 4 + k):
        dist[int(data[i])] = -2                 # -2 = cam
    if dist[T] == -2:
        res = -1
    else:
        luy = [10**i for i in range(n)]
        dist[S] = 0
        q = deque([S])
        while q and dist[T] < 0:
            x = q.popleft()
            d = dist[x] + 1
            for p in luy:
                c = x // p % 10
                y = x + p if c < 9 else x - 9 * p
                if dist[y] == -1:
                    dist[y] = d; q.append(y)
                y = x - p if c > 0 else x + 9 * p
                if dist[y] == -1:
                    dist[y] = d; q.append(y)
        res = dist[T]
    with open('MAKHOA.OUT', 'w') as f:
        f.write(str(res) + '\n')

main()
