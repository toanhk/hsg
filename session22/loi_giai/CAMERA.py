# CAMERA (de thi thu so 2, bai 3, 7 diem) - QHD tren cay 3 trang thai (buoi 19)
# Cay n nut. Dat camera o nut v ton c[v]; camera o v giam sat v va moi nut ke v. Moi nut phai duoc giam sat.
# Tong chi phi nho nhat? n <= 10^5, 1 <= c[v] <= 10^4.
# QHD (goc 1, xu ly con truoc cha):
#   Trang thai : A[v] = v CO camera;
#                B[v] = v khong camera, da duoc mot CON giam sat;
#                C[v] = v khong camera, chua ai giam sat (cha PHAI dat camera).
#                Ca ba deu yeu cau moi nut trong cay con cua v (tru chinh v o C) da duoc giam sat.
#   Cong thuc  : A[v] = c[v] + tong min(A[u], B[u], C[u])     (con u nao cung duoc v giam sat)
#                C[v] = tong B[u]                               (khong con nao co camera; con phai tu lo)
#                B[v] = tong min(A[u], B[u]), co it nhat mot con chon A:
#                       = S + max(0, min_u (A[u] - B[u]))  voi S = tong min(A[u], B[u]).
#   Khoi tao   : la: A = c, B = vo cung (khong co con), C = 0.
#   Thu tu     : duyet nguoc thu tu BFS/DFS tu goc (khong de quy).
#   Dap an     : min(A[1], B[1]).
# O(n); do ~0,2 s voi n = 10^5.
def main():
    data = open('CAMERA.INP', 'rb').read().split()
    n = int(data[0])
    c = [0] + list(map(int, data[1:1 + n]))
    adj = [[] for _ in range(n + 1)]
    pos = 1 + n
    for _ in range(n - 1):
        u, v = int(data[pos]), int(data[pos + 1]); pos += 2
        adj[u].append(v); adj[v].append(u)
    # thu tu duyet tu goc 1 bang ngan xep (khong de quy)
    par = [0] * (n + 1); par[1] = -1
    order = []; st = [1]
    while st:
        u = st.pop(); order.append(u)
        for v in adj[u]:
            if v != par[u]:
                par[v] = u; st.append(v)
    INF = float('inf')
    A = [0] * (n + 1); B = [0] * (n + 1); C = [0] * (n + 1)
    for v in reversed(order):                       # con xong truoc cha
        a = c[v]; s = 0; cc = 0; them = INF
        for u in adj[v]:
            if u == par[v]:
                continue
            Au, Bu = A[u], B[u]
            a += min(Au, Bu, C[u])
            s += Au if Au < Bu else Bu
            cc += Bu
            if Au - Bu < them:
                them = Au - Bu
        A[v] = a
        C[v] = cc                                    # la: 0
        B[v] = s + (them if them > 0 else 0)         # la: them = INF -> B = INF
    ans = min(A[1], B[1])
    with open('CAMERA.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
