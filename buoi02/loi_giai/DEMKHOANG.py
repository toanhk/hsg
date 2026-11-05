# DEMKHOANG: q truy van "co bao nhieu a[i] nam trong [L, R]". n, q <= 2*10^5
# Sap xep 1 lan O(n log n), moi truy van 2 lan bisect O(log n)
from bisect import bisect_left, bisect_right

def main():
    data = open('DEMKHOANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = sorted(map(int, data[2:2 + n]))
    lr = list(map(int, data[2 + n:2 + n + 2 * q]))
    out = []
    for i in range(0, 2 * q, 2):
        L, R = lr[i], lr[i + 1]
        # so phan tu <= R tru so phan tu < L
        out.append(str(bisect_right(a, R) - bisect_left(a, L)))
    with open('DEMKHOANG.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
