# HAIPHE: n nguoi, chia thanh hai phe Dong va Tay (mot phe co the rong). Co m rang buoc "u v t":
#   t = 0: u va v CUNG phe;  t = 1: u va v KHAC phe.  Dem so cach chia thoa man moi rang buoc,
# lay du 10^9 + 7. n <= 10^5, m <= 2*10^5 (mot cap co the xuat hien nhieu lan, u != v).
# Mo hinh: dinh = nguoi, canh (u, v) mang trong so t. Gan phe[u] in {0, 1}; canh doi hoi
#   phe[v] = phe[u] XOR t. Day la "to hai mau co trong so": HAIPHIA la truong hop moi t = 1.
# Trong mot thanh phan lien thong, chon phe cua dinh goc la quyet dinh het moi dinh khac
# (di theo canh, XOR dan). DFS ngan xep: gap dinh da gan ma phe[v] != phe[u] ^ t -> mau thuan -> 0.
# Neu khong mau thuan: moi thanh phan co dung 2 cach (goc o Dong hoac Tay) -> dap an 2^c mod p.
# O(n + m).
MOD = 10**9 + 7

def main():
    data = open('HAIPHE.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 3 * m]))
    # ke[u] chua cac so v*2 + t (GOP v va t vao MOT so nguyen): nhanh hon luu cap (v, t)
    # vi khong phai tao 4*10^5 tuple; tach lai bang x >> 1 (= v) va x & 1 (= t).
    ke = [[] for _ in range(n + 1)]
    for u, v, t in zip(a[0::3], a[1::3], a[2::3]):
        ke[u].append(v << 1 | t)
        ke[v].append(u << 1 | t)

    phe = [-1] * (n + 1)
    c = 0
    ok = True
    for s in range(1, n + 1):
        if phe[s] != -1:
            continue
        c += 1
        phe[s] = 0                             # co dinh goc o phe 0, cuoi cung nhan 2
        st = [s]
        while st and ok:
            u = st.pop()
            pu = phe[u]
            for x in ke[u]:
                v = x >> 1
                can = pu ^ (x & 1)             # phe ma v BAT BUOC phai o
                if phe[v] == -1:
                    phe[v] = can
                    st.append(v)
                elif phe[v] != can:
                    ok = False
                    break
        if not ok:
            break

    with open('HAIPHE.OUT', 'w') as out:
        out.write(str(pow(2, c, MOD) if ok else 0) + '\n')

main()
