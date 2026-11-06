# CHUTRINH: do thi vo huong n dinh, m canh (khong khuyen, khong canh lap).
# Dem so thanh phan lien thong CO CHUA chu trinh. n <= 10^5, m <= 2*10^5.
# Y tuong: DFS bang ngan xep, nho cha[v] = dinh da phat hien ra v (canh "cay" cha[v] -- v).
# Khi xet dinh u va gap dinh ke v DA THAM ma v != cha[u] thi canh (u, v) khong phai canh cay
# -> hai dau da noi voi nhau qua cay DFS, them canh nay khep thanh chu trinh.
# (v == cha[u] la chinh canh vua di xuong u, phai bo qua; do khong co canh lap nen an toan.)
# Kiem tra lai bang dem: thanh phan k dinh, e canh co chu trinh <=> e >= k (cay co dung k-1 canh).
# O(n + m) ~0.2 s.

def main():
    data = open('CHUTRINH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)

    tham = [False] * (n + 1)
    cha = [0] * (n + 1)                        # cha[s] = 0 voi dinh goc (khong co dinh 0)
    dem = 0
    for s in range(1, n + 1):
        if tham[s]:
            continue
        tham[s] = True
        st = [s]
        co_chu_trinh = False
        while st:
            u = st.pop()
            cu = cha[u]
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True
                    cha[v] = u                 # canh cay u -- v
                    st.append(v)
                elif v != cu:                  # da tham, khong phai canh vua di xuong -> chu trinh
                    co_chu_trinh = True        # KHONG dung lai: van phai tham het thanh phan
        if co_chu_trinh:
            dem += 1

    with open('CHUTRINH.OUT', 'w') as out:
        out.write(str(dem) + '\n')

main()
