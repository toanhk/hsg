# TONGDOAN: q truy van tong a[l..r]. n <= 10^6, q <= 2*10^5. Mang cong don: O(n + q)
from itertools import accumulate

def main():
    data = open('TONGDOAN.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    # s[i] = a[1] + ... + a[i], s[0] = 0  (accumulate chay bang C, nhanh hon vong for)
    s = [0]
    s += accumulate(map(int, data[2:2 + n]))
    lr = list(map(int, data[2 + n:2 + n + 2 * q]))
    out = [str(s[lr[i + 1]] - s[lr[i] - 1]) for i in range(0, 2 * q, 2)]
    with open('TONGDOAN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
