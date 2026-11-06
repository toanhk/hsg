# DOCTHAP: n diem, m doan duong hai chieu, doan i co do doc h. Di tu s den t, chon lo trinh sao cho
# doan DOC NHAT tren lo trinh la it doc nhat. In do doc do; s = t in 0; khong di duoc in -1.
# n <= 10^5, m <= 2*10^5, h <= 10^9.
# Y tuong Kruskal: them canh theo h TANG DAN vao DSU. Ngay khi s va t vua cung thanh phan thi canh vua them
# (co h = H) la dap an: chi dung cac canh <= H da di duoc, con chi dung canh < H thi chua.
# (Tuong duong: duong di giua s va t tren CAY KHUNG NHO NHAT la duong "canh lon nhat nho nhat".)
# O(m log m).
def main():
    data = open('DOCTHAP.INP', 'rb').read().split()
    n, m, s, t = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    U = list(map(int, data[4:4 + 3 * m:3]))
    V = list(map(int, data[5:5 + 3 * m:3]))
    H = list(map(int, data[6:6 + 3 * m:3]))
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    kq = 0 if s == t else -1
    if s != t:
        for i in sorted(range(m), key=H.__getitem__):
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
            x = s                              # kiem tra s, t da cung thanh phan chua
            while parent[x] != x:
                x = parent[x]
            y = t
            while parent[y] != y:
                y = parent[y]
            if x == y:
                kq = H[i]
                break
    with open('DOCTHAP.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
