# HVCON - ban duyet TUNG O (de hieu nhat), ~0.4 s voi 1000 x 1000: sat moc, nen ban chinh HVCON.py
# day vong trong xuong C. De bai:
# HVCON: bang m x n so nguyen KHONG AM va so S. Tim canh k lon nhat sao cho co mot hinh vuong
# con k x k co tong cac o <= S (khong co thi in 0). m, n <= 1000, a <= 10^6, S <= 10^15
# Buoc 1 - mang cong don 2 chieu (QHD tren luoi):
#   P[i][j] = tong hinh chu nhat (1,1)-(i,j) = a[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
#   Tong hinh vuong canh k, goc duoi-phai (i,j):
#   P[i][j] - P[i-k][j] - P[i][j-k] + P[i-k][j-k]
#   Lam tung hang trong C: P[i] = map(add, P[i-1], accumulate(hang a, initial=0)).
# Buoc 2 - dap an chi TANG: so khong am nen hinh vuong nho hon nam trong mot hinh vuong hop le
#   cung hop le. Duyet moi o (i,j) lam goc duoi-phai, chi thu canh ans+1; dung thi tang ans va thu
#   tiep. Tong so lan thu = m*n + (so lan tang) = O(m*n).
from itertools import accumulate
from operator import add

def main():
    data = open('HVCON.INP', 'rb').read().split()
    m, n, S = int(data[0]), int(data[1]), int(data[2])
    vals = list(map(int, data[3:3 + m * n]))
    P = [[0] * (n + 1)]
    for i in range(m):
        P.append(list(map(add, P[-1], accumulate(vals[i * n:(i + 1) * n], initial=0))))
    ans = 0
    for i in range(1, m + 1):
        Pi = P[i]
        for j in range(1, n + 1):
            k = ans + 1
            while k <= i and k <= j:
                Pk = P[i - k]
                if Pi[j] - Pk[j] - Pi[j - k] + Pk[j - k] <= S:
                    ans = k
                    k += 1
                else:
                    break
    with open('HVCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
