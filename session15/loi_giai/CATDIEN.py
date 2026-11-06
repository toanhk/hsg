# CATDIEN: n tram dien, m day dien (day thu i noi u_i, v_i). Bao lam dut lan luot q day (chi so
# phan biet). Sau MOI lan dut in so vung dien (thanh phan lien thong).   n, m, q <= 10^5 (q <= m)
# DSU chi biet HOP, khong biet TACH. Meo: lam NGUOC THOI GIAN.
#   - Trang thai cuoi (sau q lan dut) = do thi gom cac day KHONG bi dut -> dung DSU tu do.
#   - Di nguoc tu lan dut thu q ve lan 1: ghi dap an hien tai, roi "noi lai" day vua dut.
#   Dut day = noi day khi nhin nguoc thoi gian. Moi day duoc hop dung mot lan: O((m + q) * alpha).
# Dap an ghi vao mang kq theo chi so roi in xuoi.

def main():
    data = open('CATDIEN.INP', 'rb').read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    U = list(map(int, data[3:3 + 2 * m:2]))
    V = list(map(int, data[4:4 + 2 * m:2]))
    cat = [int(x) - 1 for x in data[3 + 2 * m:3 + 2 * m + q]]
    bi_cat = bytearray(m)
    for e in cat:
        bi_cat[e] = 1
    cha = list(range(n + 1))
    co = [1] * (n + 1)

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    vung = n
    for e in range(m):                # trang thai sau khi da dut het q day
        if not bi_cat[e]:
            a = find(U[e]); b = find(V[e])
            if a != b:
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a
                co[a] += co[b]
                vung -= 1
    kq = [0] * q
    for i in range(q - 1, -1, -1):
        kq[i] = vung                  # so vung ngay sau lan dut thu i
        e = cat[i]                    # quay nguoc thoi gian: noi lai day thu i
        a = find(U[e]); b = find(V[e])
        if a != b:
            if co[a] < co[b]:
                a, b = b, a
            cha[b] = a
            co[a] += co[b]
            vung -= 1
    with open('CATDIEN.OUT', 'w') as f:
        f.write('\n'.join(map(str, kq)) + '\n')

main()
