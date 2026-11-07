# THU VIEN CODE MAU - SO HOC hay di kem bai dem (sang, to hop mod).
from math import gcd

MOD = 10**9 + 7

def sang(M):
    """bytearray nt[0..M], nt[x] = 1 neu x nguyen to. Gan lat cat nhanh hon vong for ~10 lan."""
    nt = bytearray([1]) * (M + 1)
    nt[0] = 0
    if M >= 1:
        nt[1] = 0
    i = 2
    while i * i <= M:
        if nt[i]:
            nt[i * i::i] = bytes(len(range(i * i, M + 1, i)))
        i += 1
    return nt

def bang_to_hop(N, mod=MOD):
    """Giai thua va nghich dao giai thua den N -> C(n, k) trong O(1). pow(x, mod - 2, mod) = nghich dao (mod nguyen to)."""
    gt = [1] * (N + 1)
    for i in range(1, N + 1):
        gt[i] = gt[i - 1] * i % mod
    ngh = [1] * (N + 1)
    ngh[N] = pow(gt[N], mod - 2, mod)
    for i in range(N, 0, -1):
        ngh[i - 1] = ngh[i] * i % mod

    def C(n, k):
        if k < 0 or k > n:
            return 0
        return gt[n] * ngh[k] % mod * ngh[n - k] % mod

    return C

def bcnn(a, b):
    return a // gcd(a, b) * b
