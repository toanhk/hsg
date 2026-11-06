# LIENTHONG: do thi vo huong n dinh, m canh. In so thanh phan lien thong va so dinh cua
# thanh phan lon nhat. n <= 10^5, m <= 2*10^5 (co the co canh lap, khuyen).
# Y tuong: lan luot xet dinh s = 1..n; neu s chua tham -> gap thanh phan MOI, dem += 1,
# roi DFS tu s bang NGAN XEP (list): moi dinh duoc danh dau ngay khi day vao nen vao ngan xep
# dung 1 lan. Tong cong O(n + m): ~0.2 s ca doc lan dung danh sach ke (xem do_dfs.py).
# Khong viet de quy: do thi duong thang 10^5 dinh lam de quy sau 10^5 tang.

def main():
    data = open('LIENTHONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]            # ke[u] = danh sach dinh ke voi u
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)

    tham = [False] * (n + 1)
    dem = 0
    lon_nhat = 0
    for s in range(1, n + 1):
        if tham[s]:
            continue
        dem += 1                               # s chua tham -> thanh phan moi
        tham[s] = True
        st = [s]                               # ngan xep: cac dinh da thay, chua xet ke
        co = 1                                 # so dinh cua thanh phan nay
        while st:
            u = st.pop()
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True             # danh dau KHI DAY vao
                    st.append(v)
                    co += 1
        if co > lon_nhat:
            lon_nhat = co

    with open('LIENTHONG.OUT', 'w') as out:
        out.write(f'{dem} {lon_nhat}\n')

main()
