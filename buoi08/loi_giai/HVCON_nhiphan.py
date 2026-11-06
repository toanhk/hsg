# HVCON - ban trung gian: mang cong don + chat nhi phan canh k (co hinh vuong k hop le thi moi
# k' < k cung co). Moi lan kiem tra mot k mat O(m*n) -> tong O(m*n*log). Qua subtask 2 (<= 300),
# subtask 3 (1000 x 1000) thi ~10 lan x 10^6 o -> cham.
from itertools import accumulate
from operator import add

def main():
    data = open('HVCON.INP', 'rb').read().split()
    m, n, S = int(data[0]), int(data[1]), int(data[2])
    vals = list(map(int, data[3:3 + m * n]))
    P = [[0] * (n + 1)]
    for i in range(m):
        P.append(list(map(add, P[-1], accumulate(vals[i * n:(i + 1) * n], initial=0))))

    def co(k):                                 # co hinh vuong canh k tong <= S khong?
        for i in range(k, m + 1):
            Pi, Pk = P[i], P[i - k]
            for j in range(k, n + 1):
                if Pi[j] - Pk[j] - Pi[j - k] + Pk[j - k] <= S:
                    return True
        return False

    lo, hi = 0, min(m, n)                      # co(lo) dung (k = 0 luon dung)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if co(mid):
            lo = mid
        else:
            hi = mid - 1
    with open('HVCON.OUT', 'w') as f:
        f.write(str(lo) + '\n')

main()
