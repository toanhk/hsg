# TORAO: to n cot hang rao, moi cot 1 trong k mau, KHONG co 3 cot lien tiep cung mau.
# Dem so cach mod 10^9+7. n <= 10^6, k <= 2*10^9
# Chi biet "so cach to i cot" chua du de di tiep: can biet cot i co cung mau cot i-1 khong.
# -> them mot chieu nho (2 gia tri) vao trang thai.
#   Trang thai : khac[i] = so cach to i cot, cot i KHAC mau cot i-1
#                giong[i] = so cach to i cot, cot i GIONG mau cot i-1
#   Truy hoi   : khac[i]  = (khac[i-1] + giong[i-1]) * (k - 1)   (chon 1 trong k-1 mau khac cot i-1)
#                giong[i] = khac[i-1]                            (chi duoc lap mau neu 2 cot truoc khac nhau)
#   Khoi tao   : khac[1] = k, giong[1] = 0
#   Thu tu     : i tang dan
#   Dap an     : khac[n] + giong[n]
MOD = 10**9 + 7

def main():
    data = open('TORAO.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    k1 = (k - 1) % MOD
    khac, giong = k % MOD, 0
    for _ in range(n - 1):
        khac, giong = (khac + giong) * k1 % MOD, khac
    with open('TORAO.OUT', 'w') as out:
        out.write(str((khac + giong) % MOD) + '\n')

main()
