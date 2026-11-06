# QUYNHOM: n ban, ban i co a[i] dong (<= 10^9). q thao tac:
#   "1 u v": nhom cua u va nhom cua v gop quy lam mot (cung nhom roi thi khong doi gi)
#   "2 u x": ban u bo them x dong vao quy (x <= 10^9)
#   "3 u"  : in tong quy cua nhom chua u.          n, q <= 2*10^5
# DSU giu THONG TIN O GOC: tong[r] = tong tien cua ca nhom co goc r.
#   - hop a, b (a != b): tong[a] += tong[b]  (b khong con la goc, tong[b] bo di khong dung nua)
#   - bo tien: tong[find(u)] += x  (KHONG phai tong[u]: u co the khong con la goc)
#   - BAT BUOC kiem tra a != b truoc khi cong, neu khong quy bi cong doi (xem QUYNHOM_sai.py).
# Moi dong input co 2 hoac 3 so -> doc bang con tro pos theo loai thao tac.

def main():
    data = open('QUYNHOM.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    cha = list(range(n + 1))
    co = [1] * (n + 1)
    tong = [0] + list(map(int, data[2:2 + n]))
    pos = 2 + n

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    out = []
    for _ in range(q):
        t = data[pos]
        if t == b'1':
            a = find(int(data[pos + 1])); b = find(int(data[pos + 2])); pos += 3
            if a != b:
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a
                co[a] += co[b]
                tong[a] += tong[b]
        elif t == b'2':
            tong[find(int(data[pos + 1]))] += int(data[pos + 2]); pos += 3
        else:
            out.append(str(tong[find(int(data[pos + 1]))])); pos += 2
    with open('QUYNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
