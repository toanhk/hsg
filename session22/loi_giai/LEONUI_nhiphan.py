# LEONUI - chat nhi phan dap an D + BFS chi di qua canh co chenh lech <= D.
# "Di duoc voi D" la tinh chat don dieu (D lon hon thi cang de) nen chat nhi phan duoc.
# log2(10^6) = 20 lan BFS tren m*n o: kip subtask 1-2 (m, n <= 100), 300 x 300 thi ~2 s -> qua gio.
from collections import deque

def main():
    data = open('LEONUI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    h = list(map(int, data[2:2 + m * n]))
    N = m * n

    def di_duoc(D):
        seen = bytearray(N); seen[0] = 1
        q = deque([0])
        while q:
            p = q.popleft()
            if p == N - 1:
                return True
            i, j = divmod(p, n)
            for ok, r in ((i > 0, p - n), (i < m - 1, p + n), (j > 0, p - 1), (j < n - 1, p + 1)):
                if ok and not seen[r] and abs(h[p] - h[r]) <= D:
                    seen[r] = 1; q.append(r)
        return False

    lo, hi = 0, 10**6                    # di_duoc(hi) luon dung
    while lo < hi:
        mid = (lo + hi) // 2
        if di_duoc(mid):
            hi = mid
        else:
            lo = mid + 1
    with open('LEONUI.OUT', 'w') as f:
        f.write(str(lo) + '\n')

main()
