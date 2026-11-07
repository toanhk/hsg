# DEMLOTRINH: DAG n dinh, m cung (co the co cung lap - moi cung la mot lo trinh khac nhau). Dem so duong di
# tu 1 den n, in theo modulo 10^9 + 7. n, m <= 2*10^5.
#   Trang thai : c[v] = so duong di tu 1 den v (mod P)
#   Truy hoi   : c[v] = tong c[u] voi moi cung u -> v
#   Khoi tao   : c[1] = 1, cac dinh khac 0
#   Thu tu     : thu tu to-po (Kahn): khi lay u ra, c[u] da du (moi cung vao u da cong xong)
#   Dap an     : c[n]
# So duong di co the toi 2^(n-1) (moi dinh noi toi moi dinh sau no) -> bat buoc lay modulo.
# Lay % mot lan khi u duoc lay ra (c[u] da du) thay vi % o moi phep cong: nhanh hon, so van nho.  O(n + m)
P = 10**9 + 7

def main():
    data = list(map(int, open('DEMLOTRINH.INP', 'rb').read().split()))
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    it = iter(data[2:2 + 2 * m])
    for u, v in zip(it, it):
        adj[u].append(v); deg[v] += 1
    c = [0] * (n + 1)
    c[1] = 1
    q = [u for u in range(1, n + 1) if deg[u] == 0]
    for u in q:
        cu = c[u] % P                       # c[u] da chot: chi lay du mot lan o day
        c[u] = cu
        for v in adj[u]:
            c[v] += cu                      # c[v] tang toi da deg_vao(v) * P: van la so nho
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    with open('DEMLOTRINH.OUT', 'w') as fo:
        fo.write(str(c[n] % P) + '\n')

main()
