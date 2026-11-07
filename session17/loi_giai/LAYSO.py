# LAYSO: day n so nguyen duong a[0..n-1] tren ban. An va Binh lan luot choi, An di truoc; moi luot nguoi choi
# lay MOT so o DAU TRAI hoac DAU PHAI cua day con lai va cong vao diem minh. Ca hai deu choi toi uu
# (moi nguoi muon diem minh tru diem doi thu lon nhat). In tong diem cua An.
# n <= 2000, a[i] <= 10^9.
# QHD tren doan (tro choi hai nguoi -> luu CHENH LECH):
#   Trang thai : f[l][r] = (diem nguoi DANG DI) - (diem doi thu) khi day con lai la a[l..r], ca hai toi uu
#   Truy hoi   : lay a[l] thi doi thu thanh nguoi dang di tren a[l+1..r]:
#                f[l][r] = max(a[l] - f[l+1][r], a[r] - f[l][r-1])
#   Khoi tao   : f[i][i] = a[i]
#   Thu tu     : l giam dan, r tang dan tu l+1 -> chi can hang l+1 -> giu 2 hang (bo nho O(n))
#   Dap an     : An - Binh = f[0][n-1], An + Binh = tong -> An = (tong + f[0][n-1]) / 2
# O(n^2/2) = 2*10^6 o voi n = 2000. Do: ~0,19 s (giu 1 hang), 0,24 s (bang 2 chieu).
def main():
    data = open('LAYSO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    sau = [0] * n                              # sau[r] = f[l+1][r]
    for l in range(n - 1, -1, -1):
        x = a[l]
        hang = [0] * n
        hang[l] = x
        c = x                                  # c = f[l][r-1]
        for r in range(l + 1, n):
            u = x - sau[r]                     # lay dau trai
            v = a[r] - c                       # lay dau phai
            c = u if u > v else v
            hang[r] = c
        sau = hang
    with open('LAYSO.OUT', 'w') as out:
        out.write(str((sum(a) + sau[n - 1]) // 2) + '\n')

main()
