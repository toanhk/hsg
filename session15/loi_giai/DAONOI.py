# DAONOI: bien R x C luc dau toan nuoc. Lan luot k lan, o (i, j) noi len thanh dat (o da la dat
# roi thi khong doi gi). Sau MOI lan in so dao (nhom o dat chung canh, 4 huong).
# R * C <= 10^6, k <= 2*10^5
# DSU tren o luoi: ma hoa o (i, j) thanh MOT so p = i * W + j voi W = C + 2 (luoi co VIEN nuoc
#   bao quanh, nhu buoi 11) -> 4 o ke la p - 1, p + 1, p - W, p + W, khong can kiem tra bien.
# O moi noi len: dao += 1, roi voi moi o ke da la dat ma khac goc: hop, dao -= 1.
# Mang cha co (R + 2) * W ~ 10^6 phan tu: list(range(...)) tao mat ~0,02 giay.

def main():
    data = open('DAONOI.INP', 'rb').read().split()
    R, C, k = int(data[0]), int(data[1]), int(data[2])
    W = C + 2
    N = (R + 2) * W
    dat = bytearray(N)                 # 1 = dat; vien luon la 0 (nuoc)
    cha = list(range(N))
    co = [1] * N

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    dao = 0
    out = []
    for t in range(3, 3 + 2 * k, 2):
        p = int(data[t]) * W + int(data[t + 1])
        if not dat[p]:
            dat[p] = 1
            dao += 1
            for v in (p - 1, p + 1, p - W, p + W):
                if dat[v]:
                    a = find(p); b = find(v)
                    if a != b:
                        if co[a] < co[b]:
                            a, b = b, a
                        cha[b] = a
                        co[a] += co[b]
                        dao -= 1
        out.append(str(dao))
    with open('DAONOI.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
