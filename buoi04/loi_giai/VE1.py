# VE1: tu n ve 1 bang it thao tac nhat: n -> n-1 ; n -> n/2 (n chan) ; n -> n/3 (n chia het 3).
# T truy van, n <= 10^18 -> khong the lap bang 10^18 o. Dung QHD CO NHO tren cac trang thai thua.
# Nhan xet: truoc khi chia 2 chi can tru dung n % 2 lan, truoc khi chia 3 chi can tru n % 3 lan.
#   (Tru 2 lan roi chia 2 = chia 2 roi tru 1 lan: ton 3 buoc thay vi 2. Tuong tu voi 3.)
#   Trang thai : f(n) = so thao tac it nhat de tu n ve 1
#   Truy hoi   : f(n) = 1 + min( n%2 + f(n//2), n%3 + f(n//3) )   voi n >= 4
#   Khoi tao   : f(1) = 0, f(2) = 1, f(3) = 1
#   Thu tu     : de quy co nho (dict) - chi cham cac so dang n // (2^a * 3^b): ~ 60*40 trang thai
#   Dap an     : f(n)
# Do sau de quy <= log2(10^18) ~ 60 -> khong lo tran. Dict 'nho' dung chung cho moi truy van.
def main():
    data = open('VE1.INP', 'rb').read().split()
    t = int(data[0])
    nho = {1: 0, 2: 1, 3: 1}

    def f(n):
        if n in nho:
            return nho[n]
        r = 1 + min(n % 2 + f(n // 2), n % 3 + f(n // 3))
        nho[n] = r
        return r

    kq = [str(f(int(x))) for x in data[1:1 + t]]
    with open('VE1.OUT', 'w') as out:
        out.write('\n'.join(kq) + '\n')

main()
