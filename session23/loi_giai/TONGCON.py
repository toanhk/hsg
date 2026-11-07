# TONGCON (de thi thu so 3, bai 1, 6 diem) - hai con tro + "dem <= X" de tranh sai bien
# Day n so KHONG AM a[i]. Dem so doan con a[l..r] co tong nam trong [L, R].
# n <= 5*10^5, 0 <= a[i] <= 10^9, 0 <= L <= R <= 10^15.
# Meo chong sai bien: dem(X) = so doan co tong <= X. Dap an = dem(R) - dem(L - 1)  (dem(-1) = 0).
#   Vi a[i] >= 0 nen khi r tang, l nho nhat co tong(l..r) <= X chi tang -> hai con tro O(n).
# Do: 2 lan quet 5*10^5 phan tu ~0,17 s, ca bai ~0,3 s.
# Bay: dem(R) - dem(L) (mat cac doan tong dung bang L - xem TONGCON_sai.py), a[i] = 0 lam nhieu doan
#      cung tong, L = 0, dap an toi n(n+1)/2 ~ 1,25*10^11 (C++/Pascal phai dung int64).
def main():
    data = open('TONGCON.INP', 'rb').read().split()
    n, L, R = int(data[0]), int(data[1]), int(data[2])
    a = list(map(int, data[3:3 + n]))

    def dem(X):                       # so doan con co tong <= X
        if X < 0:
            return 0
        res = 0; l = 0; s = 0
        for r in range(n):
            s += a[r]
            while s > X:              # thu hep tu trai cho den khi tong <= X
                s -= a[l]; l += 1
            res += r - l + 1          # moi l' trong [l, r] deu cho tong(l'..r) <= X
        return res

    ans = dem(R) - dem(L - 1)
    with open('TONGCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
