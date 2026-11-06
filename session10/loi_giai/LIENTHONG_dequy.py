# LIENTHONG - ban DE QUY (de chua tren lop): dung tren do thi ngau nhien, nhung tren do thi
# DUONG THANG 1-2-...-n thi do sau de quy = n.
#  - Khong co setrecursionlimit: RecursionError tu do sau ~1000 (Test07, Test09).
#  - Co setrecursionlimit(10**6): Python 3.12+ tren Linux chay duoc; Python 3.8-3.11
#    (hay gap o phong thi, nhat la tren Windows) vo ngan xep C -> chuong trinh chet khong bao loi.
# => Quy tac cua lop: DFS luon viet bang ngan xep (xem LIENTHONG.py).

def main():
    data = open('LIENTHONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)
    tham = [False] * (n + 1)

    def dfs(u):                                # tra ve so dinh tham duoc tu u
        tham[u] = True
        co = 1
        for v in ke[u]:
            if not tham[v]:
                co += dfs(v)
        return co

    dem = lon_nhat = 0
    for s in range(1, n + 1):
        if not tham[s]:
            dem += 1
            lon_nhat = max(lon_nhat, dfs(s))
    with open('LIENTHONG.OUT', 'w') as out:
        out.write(f'{dem} {lon_nhat}\n')

main()
