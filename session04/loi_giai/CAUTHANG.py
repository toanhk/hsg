# CAUTHANG: tu mat dat (bac 0) len bac n, moi buoc 1, 2 hoac 3 bac, khong dat chan len bac hong.
# Dem so cach mod 10^9+7. n <= 10^6
#   Trang thai : f[i] = so cach dung dung tren bac i
#   Truy hoi   : f[i] = 0 neu bac i hong, nguoc lai f[i-1] + f[i-2] + f[i-3]
#   Khoi tao   : f[0] = 1 (dung yen o mat dat la 1 cach); bac am coi nhu 0 cach
#   Thu tu     : i tang dan
#   Dap an     : f[n]
# Mang f lech 3 o (f[i] luu o vi tri i + 3) de khong phai xu ly rieng i = 1, 2.
MOD = 10**9 + 7

def main():
    data = open('CAUTHANG.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    hong = bytearray(n + 4)             # hong[i + 3] = 1 neu bac i hong
    for x in data[2:2 + k]:
        hong[int(x) + 3] = 1
    f = [0] * (n + 4)
    f[3] = 1                            # bac 0
    for i in range(4, n + 4):
        if not hong[i]:
            f[i] = (f[i - 1] + f[i - 2] + f[i - 3]) % MOD
    with open('CAUTHANG.OUT', 'w') as out:
        out.write(str(f[n + 3]) + '\n')

main()
