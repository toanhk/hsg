# NOILANG - ban SAI de chua: find DE QUY va KHONG hop theo kich thuoc (luon gan parent[a] = b).
# Voi test duong thang "1-2, 2-3, 3-4, ..." xep theo chi phi tang dan, cay DSU thanh mot xich dai n:
#   - khong nen duong: moi find di het xich -> O(n^2);
#   - co nen duong nhung de quy: lan find dau tien tren xich dai 10^5 -> RecursionError.
# Bai hoc: find phai viet bang vong lap (va nen hop theo kich thuoc).
import sys
sys.setrecursionlimit(10000)

def main():
    data = open('NOILANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = sorted((int(data[i + 2]), int(data[i]), int(data[i + 1])) for i in range(2, 2 + 3 * m, 3))
    parent = list(range(n + 1))

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    tong = 0; chon = 0
    for w, u, v in canh:
        a = find(u); b = find(v)
        if a != b:
            parent[a] = b                      # luon gan a vao b -> xich dai
            tong += w; chon += 1
    with open('NOILANG.OUT', 'w') as f:
        f.write(str(tong if chon == n - 1 else -1) + '\n')

main()
