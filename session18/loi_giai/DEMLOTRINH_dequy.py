# DEMLOTRINH - ban DE QUY CO NHO (dung y tuong, chay dung voi do thi "nong"): dem(u) = so duong tu u den n
#   dem(n) = 1, dem(u) = tong dem(v) voi u -> v, nho ket qua trong mang.
# Van de: do sau de quy = do dai duong di dai nhat. Test "chuoi" 1 -> 2 -> ... -> 2*10^5 lam de quy sau
# 2*10^5 tang: RecursionError, hoac vo ngan xep C (chuong trinh chet khong bao loi) tren Windows/Python cu
# du da setrecursionlimit. Bai hoc: QHD tren DAG viet theo thu tu to-po bang vong lap (DEMLOTRINH.py).
import sys

P = 10**9 + 7

def main():
    sys.setrecursionlimit(10**6)
    data = list(map(int, open('DEMLOTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[data[2 + 2 * i]].append(data[3 + 2 * i])
    nho = [-1] * (n + 1)

    def dem(u):
        if u == n:
            return 1
        if nho[u] >= 0:
            return nho[u]
        s = 0
        for v in adj[u]:
            s += dem(v)
        nho[u] = s % P
        return nho[u]

    with open('DEMLOTRINH.OUT', 'w') as fo:
        fo.write(str(dem(1)) + '\n')

main()
