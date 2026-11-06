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
# Buoc 3 - day vong trong xuong C: voi hang i va canh k = ans+1, tong moi hinh vuong goc (i, j),
#   j = k..n, la (Pi[j] - Pk[j]) - (Pi[j-k] - Pk[j-k]) -> 3 lan map(sub, ...) roi min(). Nho nhat <= S
#   thi ans tang va thu lai CUNG hang voi canh lon hon. Ban duyet tung o: HVCON_tungo.py.
from itertools import accumulate
from operator import add, sub

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
        while ans < i and ans < n:
            k = ans + 1
            Pk = P[i - k]
            cot = map(sub, Pi, Pk)                        # cot[j] = Pi[j] - Pk[j]: tong dai k hang
            cot = list(cot)
            if min(map(sub, cot[k:], cot[:n + 1 - k])) <= S:
                ans = k
            else:
                break
    with open('HVCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
