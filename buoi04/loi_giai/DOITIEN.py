# DOITIEN: dem so cach doi S dong bang m loai to tien (moi loai dung bao nhieu to cung duoc),
# hai cach chi khac thu tu to coi la MOT cach. Mod 10^9+7. m <= 30, S <= 10^5
#   Trang thai : f[s] = so cach tao tong s chi bang cac loai DA XET
#   Truy hoi   : xet them loai c: f[s] += f[s - c]  (s tang dan -> loai c dung lai duoc nhieu to)
#   Khoi tao   : f[0] = 1 (khong lay to nao), f[s > 0] = 0
#   Thu tu     : vong NGOAI la loai tien, vong TRONG la s tang dan
#   Dap an     : f[S]
# Dao 2 vong (s ngoai, loai trong) se dem ca thu tu: 1+2 va 2+1 thanh 2 cach -> SAI (do la bai CAUTHANG!)
# O(m * S) = 3*10^6 o ~ 0.3 s
MOD = 10**9 + 7

def main():
    data = open('DOITIEN.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + m]))
    f = [0] * (S + 1)
    f[0] = 1
    for x in c:
        for s in range(x, S + 1):
            f[s] = (f[s] + f[s - x]) % MOD
    with open('DOITIEN.OUT', 'w') as out:
        out.write(str(f[S]) + '\n')

main()
