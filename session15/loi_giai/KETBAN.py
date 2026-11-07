# KETBAN: n nguoi, q thao tac. "1 u v": u va v ket ban (ban cua ban cung la ban, cung nhom).
# "2 u v": hoi u va v co cung nhom khong -> in CO / KHONG.   n, q <= 2*10^5
# DSU (Disjoint Set Union): moi nhom la mot cay, goc cay dai dien cho nhom.
#   find(x): di len cha den goc. NEN DUONG: cho moi dinh tren duong di tro thang vao goc.
#   union(a, b): noi goc cay NHO vao goc cay LON (hop theo kich thuoc) -> cay cao <= log2(n).
# find viet bang VONG LAP (khong de quy): chuoi dai 2*10^5 khong lam tran ngan xep.
# Ca hai ky thuat cung nhau: moi thao tac gan nhu O(1) (O(alpha(n))). Tong O(n + q).

def main():
    data = open('KETBAN.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    cha = list(range(n + 1))           # cha[x] = x  <=>  x la goc
    co = [1] * (n + 1)                 # co[r] = so nguoi trong nhom co goc r (chi dung o goc)

    def find(x):
        r = x
        while cha[r] != r:             # 1) tim goc
            r = cha[r]
        while cha[x] != r:             # 2) nen duong: moi dinh tren duong tro thang vao goc
            cha[x], x = r, cha[x]
        return r

    out = []
    for i in range(2, 2 + 3 * q, 3):
        a = find(int(data[i + 1])); b = find(int(data[i + 2]))
        if data[i] == b'1':
            if a != b:                 # da cung nhom thi khong lam gi
                if co[a] < co[b]:
                    a, b = b, a
                cha[b] = a             # goc nho -> goc lon
                co[a] += co[b]
        else:
            out.append('CO' if a == b else 'KHONG')
    with open('KETBAN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
