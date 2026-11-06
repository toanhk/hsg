# DEMKHOANG - subtask 2: 0 <= a[i], L, R <= 10^6. Mang dem + cong don, khong can sap xep
from itertools import accumulate

def main():
    data = open('DEMKHOANG.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    V = 10**6
    cnt = [0] * (V + 1)
    for x in map(int, data[2:2 + n]):
        cnt[x] += 1
    s = [0]
    s += accumulate(cnt)        # s[v + 1] = so phan tu <= v
    lr = list(map(int, data[2 + n:2 + n + 2 * q]))
    out = [str(s[lr[i + 1] + 1] - s[lr[i]]) for i in range(0, 2 * q, 2)]
    with open('DEMKHOANG.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
