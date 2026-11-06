# MANGDIEN: n lang can co dien. Xay tram phat dien ngay tai lang i ton c[i]; keo day giua hai lang u, v
# (m tuyen kha thi) ton w. Mot lang co dien neu co tram hoac noi (qua cac day) toi lang co tram.
# Tong chi phi nho nhat de MOI lang co dien. n <= 10^5, m <= 2*10^5, c, w <= 10^9.
# Meo DINH AO: them "nha may" la dinh 0, xay tram tai i = keo day 0 - i gia c[i].
# Moi phuong an hop le <=> mot do thi con lien thong n+1 dinh (moi lang noi ve dinh 0) -> dap an la
# CAY KHUNG NHO NHAT cua do thi n+1 dinh, m+n canh. Luon co dap an (moi lang tu xay tram).
# O((m + n) log(m + n)).
def main():
    data = open('MANGDIEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + n]))
    p = 2 + n
    U = list(map(int, data[p:p + 3 * m:3])) + [0] * n          # canh that + n canh tu dinh ao 0
    V = list(map(int, data[p + 1:p + 3 * m:3])) + list(range(1, n + 1))
    W = list(map(int, data[p + 2:p + 3 * m:3])) + c
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    tong = 0; chon = 0
    for i in sorted(range(m + n), key=W.__getitem__):
        a = U[i]
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        b = V[i]
        while parent[b] != b:
            parent[b] = parent[parent[b]]; b = parent[b]
        if a == b:
            continue
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a; size[a] += size[b]
        tong += W[i]; chon += 1
        if chon == n:                          # cay khung n+1 dinh co n canh
            break
    with open('MANGDIEN.OUT', 'w') as f:
        f.write(str(tong) + '\n')

main()
