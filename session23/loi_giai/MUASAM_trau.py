# MUASAM - vet can (n <= 10): moi mon "mua" hoac "khong", loai cach mua 2 mon cung nhom hoac vuot B.
def main():
    data = open('MUASAM.INP', 'rb').read().split()
    n, B = int(data[0]), int(data[1])
    m = [tuple(map(int, data[2 + 3 * i:5 + 3 * i])) for i in range(n)]
    best = 0
    for mask in range(1 << n):
        da = set(); tien = 0; hl = 0; ok = True
        for i in range(n):
            if mask >> i & 1:
                g, w, v = m[i]
                if g in da:
                    ok = False; break
                da.add(g); tien += w; hl += v
        if ok and tien <= B and hl > best:
            best = hl
    with open('MUASAM.OUT', 'w') as fo:
        fo.write(str(best) + '\n')

main()
