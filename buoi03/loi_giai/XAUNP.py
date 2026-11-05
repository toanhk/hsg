# XAUNP: liet ke xau nhi phan do dai n khong co hai so 1 dung canh nhau, thu tu tu dien
# Quay lui: o vi tri i thu dat '0' truoc roi '1'; chi dat '1' khi o truoc khong phai '1' (cat nhanh)
# So xau = Fib(n+2); n <= 24 -> 121393 xau. Do sau de quy chi n -> an toan
import sys

def main():
    data = open('XAUNP.INP', 'rb').read().split()
    n = int(data[0])
    x = ['0'] * n            # xau dang xay dung
    kq = []                  # gom ket qua, ghi mot lan

    def thu(i):              # dien vi tri i (0..n-1)
        if i == n:
            kq.append(''.join(x))
            return
        x[i] = '0'
        thu(i + 1)
        if i == 0 or x[i - 1] == '0':
            x[i] = '1'
            thu(i + 1)
            x[i] = '0'       # tra lai trang thai (o day khong bat buoc, nhung nen tap thoi quen)

    thu(0)
    with open('XAUNP.OUT', 'w') as f:
        f.write(str(len(kq)) + '\n' + '\n'.join(kq) + '\n')

main()
