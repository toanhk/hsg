# DEMNHOM: n hon dao, chua co cau. Lan luot xay m cay cau, cau thu i noi dao u va v.
# Sau MOI cay cau in 2 so: so nhom dao (di lai duoc voi nhau) va so dao cua nhom dong nhat.
# n, m <= 2*10^5
# DSU + 2 bien: nhom = n luc dau, moi lan hop THAT SU (hai goc khac nhau) thi nhom -= 1.
#   Kich thuoc nhom chi TANG, nen nhom lon nhat chi can cap nhat bang max sau moi lan hop,
#   khong phai quet lai ca mang co[] (quet lai la O(n*m), xem DEMNHOM_quet.py).

def main():
    data = open('DEMNHOM.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    cha = list(range(n + 1))
    co = [1] * (n + 1)

    def find(x):
        r = x
        while cha[r] != r:
            r = cha[r]
        while cha[x] != r:
            cha[x], x = r, cha[x]
        return r

    nhom, lon = n, 1
    out = []
    for i in range(2, 2 + 2 * m, 2):
        a = find(int(data[i])); b = find(int(data[i + 1]))
        if a != b:
            if co[a] < co[b]:
                a, b = b, a
            cha[b] = a
            co[a] += co[b]
            nhom -= 1
            if co[a] > lon:
                lon = co[a]
        out.append(f'{nhom} {lon}')
    with open('DEMNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
