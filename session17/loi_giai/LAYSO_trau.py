# LAYSO - vet can (n <= 20): de quy minimax KHONG nho, 2^n nhanh. Tra ve diem nguoi dang di tren a[l..r]
# = tong(a[l..r]) - diem tot nhat cua doi thu sau khi minh lay.
def main():
    data = open('LAYSO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    def diem(l, r, tong):
        if l > r:
            return 0
        return tong - min(diem(l + 1, r, tong - a[l]), diem(l, r - 1, tong - a[r]))
    with open('LAYSO.OUT', 'w') as out:
        out.write(str(diem(0, n - 1, sum(a))) + '\n')

main()
