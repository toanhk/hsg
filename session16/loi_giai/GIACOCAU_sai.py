# GIACOCAU - ban SAI de chua: hop canh bat buoc truoc nhung QUEN kiem tra chung tao chu trinh
# (canh bat buoc thua bi bo qua lang le nhu canh thuong). Khi cac cau bat buoc co vong, dap an phai la -1
# nhung chuong trinh van in mot tong (cua cay khong chua du cac cau bat buoc).
def main():
    data = open('GIACOCAU.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[i]), int(data[i + 1]), int(data[i + 2]), data[i + 3]) for i in range(2, 2 + 4 * m, 4)]
    canh.sort(key=lambda e: (e[3] != b'1', -e[2]))    # bat buoc truoc, roi w giam dan
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    tong = 0; chon = 0
    for u, v, w, t in canh:
        a = find(u); b = find(v)
        if a != b:
            parent[a] = b; tong += w; chon += 1
    with open('GIACOCAU.OUT', 'w') as f:
        f.write(str(tong if chon == n - 1 else -1) + '\n')

main()
