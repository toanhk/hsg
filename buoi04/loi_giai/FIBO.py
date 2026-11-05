# FIBO: T truy van, moi truy van in F(n) mod 10^9+7. T <= 10^5, n <= 10^6
# QHD bang (bottom-up): tinh F[0..maxn] MOT LAN roi tra loi moi truy van trong O(1)
#   Trang thai : F[i] = so Fibonacci thu i (mod)
#   Truy hoi   : F[i] = F[i-1] + F[i-2]
#   Khoi tao   : F[0] = 0, F[1] = 1
#   Thu tu     : i tang dan (F[i] chi can 2 o dung truoc)
#   Dap an     : F[n] cho tung truy van
# O(maxn + T): 10^6 phep cong + mod ~ 0.1 s
MOD = 10**9 + 7

def main():
    data = open('FIBO.INP', 'rb').read().split()
    t = int(data[0])
    q = list(map(int, data[1:1 + t]))
    m = max(max(q), 1)
    F = [0] * (m + 1)
    F[1] = 1
    for i in range(2, m + 1):
        F[i] = (F[i - 1] + F[i - 2]) % MOD
    with open('FIBO.OUT', 'w') as f:
        f.write('\n'.join(str(F[n]) for n in q) + '\n')

main()
