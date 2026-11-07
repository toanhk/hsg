# TIENQUYET - ban CHAM de chua (dung, nhung qua thoi gian o subtask 3):
# moi dp[u] luon dai k+2 va gop bang hai vong 0..k x 0..k -> moi lan gop O(k^2), tong O(n*k^2).
# Voi n = k = 2000 la ~8*10^9 phep -> khong the. Du cho subtask n <= 200 (~8*10^6).
# Sua: chi lap toi so dinh thuc su co trong cay con (xem TIENQUYET.py).
NEG = -10**18

def main():
    data = open('TIENQUYET.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    c = [0] * (n + 1); p = [-1] * (n + 1)
    con = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        p[i] = int(data[2 * i]); c[i] = int(data[2 * i + 1])
        con[p[i]].append(i)
    K = k + 1
    order = [0]
    for u in order:
        order.extend(con[u])
    dp = [None] * (n + 1)
    for u in range(n + 1):
        dp[u] = [0, c[u]] + [NEG] * (K - 1)
    for u in reversed(order):
        if u == 0:
            break
        a = dp[p[u]]; b = dp[u]
        moi = a[:]
        for i in range(1, K + 1):
            for t in range(1, K + 1 - i):
                if a[i] > NEG and b[t] > NEG and a[i] + b[t] > moi[i + t]:
                    moi[i + t] = a[i] + b[t]
        dp[p[u]] = moi
    with open('TIENQUYET.OUT', 'w') as f:
        f.write(str(dp[0][K]) + '\n')

main()
