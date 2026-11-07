# TIENQUYET: n mon hoc, phai chon DUNG k mon. Mon i co diem loi ich c[i] (co the AM) va mon tien quyet p[i]
# (p[i] = 0: khong co); chon mon i thi phai chon ca p[i]. Quan he tien quyet khong co vong.
# Tim tong loi ich lon nhat. n <= 2000, 1 <= k <= n, |c[i]| <= 10^4.
# Rung cay -> them goc AO 0 (c = 0) lam cha moi mon khong co tien quyet; goc 0 luon duoc chon -> chon k+1 dinh.
# "Cai tui tren cay":
#   trang thai : dp[u][j] = tong lon nhat khi chon j dinh trong cay con u (j >= 1 thi u bat buoc duoc chon)
#   truy hoi   : gop lan luot tung con v vao u (nhu tui: moi con la mot "nhom", chon t dinh tu nhom do):
#                moi[i + t] = max(dp[u][i] + dp[v][t]),  i >= 1, t >= 0
#   khoi tao   : dp[u] = [0, c[u]] (chua gop con nao: chon 0 dinh, hoac chon rieng u)
#   thu tu     : con truoc cha -> duyet nguoc thu tu BFS tu goc 0
#   dap an     : dp[0][k + 1]
# CHAN KICH THUOC: do dai dp[u] khong vuot (so dinh da gop) va khong vuot k+1 -> tong O(n*k)
# (moi cap dinh chi "gap nhau" mot lan khi gop). Khong chan thi O(n*k^2) (xem TIENQUYET_k2.py).
# Do: n = k = 2000 khoang 0,15-0,3 s (do_cay.py).
NEG = -10**18

def main():
    data = open('TIENQUYET.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    c = [0] * (n + 1); p = [-1] * (n + 1)
    con = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        p[i] = int(data[2 * i]); c[i] = int(data[2 * i + 1])
        con[p[i]].append(i)
    K = k + 1                                  # tinh ca goc ao
    order = [0]
    for u in order:
        order.extend(con[u])
    dp = [[0, c[u]] for u in range(n + 1)]
    for u in reversed(order):
        if u == 0:
            break
        a = dp[p[u]]; b = dp[u]                # gop cay con u vao cha p[u]
        la = len(a) - 1; lb = len(b) - 1
        gioi = la + lb if la + lb < K else K
        moi = a[:gioi + 1] + [NEG] * (gioi + 1 - len(a))   # t = 0: khong lay gi tu cay con u
        for i in range(1, la + 1):
            ai = a[i]
            if ai == NEG:
                continue
            for t in range(1, min(lb, gioi - i) + 1):
                x = ai + b[t]
                if x > moi[i + t]:
                    moi[i + t] = x
        dp[p[u]] = moi
        dp[u] = None                           # giai phong bo nho
    with open('TIENQUYET.OUT', 'w') as f:
        f.write(str(dp[0][K]) + '\n')

main()
