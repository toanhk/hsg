# LICHHOC - ban SAI de chua: kiem tra "co it nhat MOT mon tien quyet da hoc" (r & t != 0 hoac t == 0)
# thay vi "MOI mon tien quyet da hoc" (r & t == t). Sai khi mot mon co >= 2 mon tien quyet.
# Test bat loi: n = 3, dieu kien 1 -> 3, 2 -> 3: dung 2 (123, 213), ban nay in 4.
def main():
    data = open('LICHHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    MOD = 10**9 + 7
    truoc = [0] * n
    for k in range(m):
        u, v = int(data[2 + 2 * k]) - 1, int(data[3 + 2 * k]) - 1
        truoc[v] |= 1 << u
    N = 1 << n
    f = [0] * N
    f[0] = 1
    for mask in range(1, N):
        s = 0
        for v in range(n):
            if mask >> v & 1:
                r = mask ^ (1 << v)
                if truoc[v] == 0 or r & truoc[v]:      # SAI
                    s += f[r]
        f[mask] = s % MOD
    with open('LICHHOC.OUT', 'w') as fo:
        fo.write(str(f[N - 1]) + '\n')

main()
