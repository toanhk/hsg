# COMBO - vet can (m <= 15): thu moi tap con cac goi (2^m), hop cac goi du n mon thi lay tong gia.
def main():
    data = open('COMBO.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    pos = 2
    s, g = [], []
    for _ in range(m):
        gia, k = int(data[pos]), int(data[pos + 1]); pos += 2
        t = 0
        for x in data[pos:pos + k]:
            t |= 1 << (int(x) - 1)
        pos += k
        s.append(t); g.append(gia)
    full = (1 << n) - 1
    best = -1
    for chon in range(1 << m):
        hop = 0; tong = 0
        for j in range(m):
            if chon >> j & 1:
                hop |= s[j]; tong += g[j]
        if hop == full and (best < 0 or tong < best):
            best = tong
    with open('COMBO.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
