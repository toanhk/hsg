# TONGKC: cay n dinh, moi canh dai 1. Voi MOI dinh u, tinh tong khoang cach tu u den tat ca cac dinh.
# n <= 2*10^5 (dap an toi ~2*10^10, Python so nguyen khong tran).
# "Doi goc" (rerooting) - hai lan duyet:
#   Lan 1 (duoi len, duyet nguoc BFS): sz[u] = kich thuoc cay con u; f[1] = tong do sau moi dinh.
#   Lan 2 (tren xuong, duyet XUOI BFS): chuyen goc tu cha p sang con v: sz[v] dinh trong cay con v
#     gan them 1, n - sz[v] dinh con lai xa them 1  =>  f[v] = f[p] + n - 2*sz[v].
# O(n) thay vi n lan BFS O(n^2).
def main():
    data = open('TONGKC.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    it = map(int, data[1:2 * n - 1])
    for u, v in zip(it, it):
        adj[u].append(v); adj[v].append(u)
    par = [0] * (n + 1); par[1] = -1
    sau = [0] * (n + 1)                        # do sau (khoang cach den goc 1)
    order = [1]
    for u in order:
        pu = par[u]; su = sau[u] + 1
        for v in adj[u]:
            if v != pu:
                par[v] = u; sau[v] = su; order.append(v)
    sz = [1] * (n + 1)
    for u in reversed(order):
        p = par[u]
        if p > 0:
            sz[p] += sz[u]
    f = [0] * (n + 1)
    f[1] = sum(sau)
    for i in range(1, n):                      # bo goc (order[0]); cha luon duoc tinh truoc con
        v = order[i]
        f[v] = f[par[v]] + n - 2 * sz[v]
    with open('TONGKC.OUT', 'w') as f_out:
        f_out.write(' '.join(map(str, f[1:])) + '\n')

main()
