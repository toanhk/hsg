# TONGCON - BAN SAI BIEN (de chua bai): lay dem(R) - dem(L) thay vi dem(R) - dem(L - 1)
# -> mat moi doan co tong DUNG BANG L. Vi du de (L = 3) da sai neu co doan tong 3.
# Bai hoc: viet "dem <= X" thi doan [L, R] = dem(R) - dem(L - 1); kiem tra bang test tay nho truoc khi nop.
def main():
    data = open('TONGCON.INP', 'rb').read().split()
    n, L, R = int(data[0]), int(data[1]), int(data[2])
    a = list(map(int, data[3:3 + n]))

    def dem(X):
        res = 0; l = 0; s = 0
        for r in range(n):
            s += a[r]
            while s > X:
                s -= a[l]; l += 1
            res += r - l + 1
        return res

    ans = dem(R) - dem(L)               # SAI: phai la dem(L - 1)
    with open('TONGCON.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
