# SONT (de khoi dong buoi 24, bai 1) - sang Eratosthenes + mang cong don
# Q truy van [L, R], dem so nguyen to trong doan. Q <= 10^5, 1 <= L <= R <= 10^6.
# Sang mot lan den max R bang bytearray + gan lat cat (nhanh hon vong for ~10 lan), cong don bang accumulate.
# Moi truy van O(1): s[R] - s[L - 1]. Do ~0,15 s.
from itertools import accumulate

def main():
    data = open('SONT.INP', 'rb').read().split()
    q = int(data[0])
    v = list(map(int, data[1:1 + 2 * q]))
    M = max(v)
    nt = bytearray([1]) * (M + 1)
    nt[0] = 0
    if M >= 1:
        nt[1] = 0
    i = 2
    while i * i <= M:
        if nt[i]:
            nt[i * i::i] = bytes(len(range(i * i, M + 1, i)))   # gach cac boi tu i*i
        i += 1
    s = list(accumulate(nt))                                     # s[x] = so nguyen to <= x
    out = [s[v[2 * k + 1]] - s[v[2 * k] - 1] for k in range(q)]  # L >= 1 nen s[L - 1] hop le
    with open('SONT.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
