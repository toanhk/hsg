# MUASAM - dung thuat toan nhung viet vong for thuan: n * B = 5*10^6 lan lap, do 0,4-0,75 s tuy may luyen tap;
# may phong thi cham hon 1,5-2 lan co the QUA 1 GIAY o test lon. So sanh voi ban map trong MUASAM.py (~0,3 s).
def main():
    data = open('MUASAM.INP', 'rb').read().split()
    n, B = int(data[0]), int(data[1])
    nhom = {}
    pos = 2
    for _ in range(n):
        g, w, v = int(data[pos]), int(data[pos + 1]), int(data[pos + 2]); pos += 3
        nhom.setdefault(g, []).append((w, v))
    f = [0] * (B + 1)
    for ds in nhom.values():
        truoc = f[:]
        for w, v in ds:
            for b in range(B, w - 1, -1):
                c = truoc[b - w] + v
                if c > f[b]:
                    f[b] = c
    with open('MUASAM.OUT', 'w') as fo:
        fo.write(str(f[B]) + '\n')

main()
