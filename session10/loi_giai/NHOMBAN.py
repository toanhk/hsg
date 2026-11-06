# NHOMBAN: n hoc sinh, m cap ban. Ban cua ban cung la ban (cung nhom). In so nhom va
# so cap hoc sinh (u < v) KHONG cung nhom. n <= 10^5, m <= 2*10^5.
# Y tuong: DFS ngan xep lay kich thuoc s1, s2, ..., sk cua tung nhom.
#   So cap khong cung nhom = tong so cap - so cap cung nhom = n(n-1)/2 - tong s_i(s_i-1)/2.
#   (Hoac cong dan: nhom thu i ghep voi tat ca nguoi o cac nhom truoc: tong s_i * da_xet.)
# n = 10^5 -> dap an toi ~5*10^9 > 2^31: Python khong tran so, nhung neu viet C++ phai dung long long.

def main():
    data = open('NHOMBAN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + 2 * m]))
    ke = [[] for _ in range(n + 1)]
    for u, v in zip(a[0::2], a[1::2]):
        ke[u].append(v)
        ke[v].append(u)

    tham = [False] * (n + 1)
    so_nhom = 0
    cap_cung_nhom = 0
    for s in range(1, n + 1):
        if tham[s]:
            continue
        so_nhom += 1
        tham[s] = True
        st = [s]
        co = 1
        while st:
            u = st.pop()
            for v in ke[u]:
                if not tham[v]:
                    tham[v] = True
                    st.append(v)
                    co += 1
        cap_cung_nhom += co * (co - 1) // 2

    with open('NHOMBAN.OUT', 'w') as out:
        out.write(f'{so_nhom}\n{n * (n - 1) // 2 - cap_cung_nhom}\n')

main()
