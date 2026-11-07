# PAIRCOUNT (HSG THPT Ninh Binh 2023-2024, ngay 06/10/2023, bai 1, 7 diem)
# Dem so cap (i, j), i < j, thoa a[i] + k = a[j].  2 <= n <= 10^6, k <= 10^9, |a[i]| <= 10^9.
# Y tuong: duyet j tu trai sang phai, dem[x] = so lan gia tri x da xuat hien O BEN TRAI j.
#   Cap (i, j) thoa man <=> a[i] = a[j] - k, nen cong dem[a[j] - k] roi moi tang dem[a[j]].
#   (Tang truoc roi moi cong thi sai khi k = 0? De cho k >= 1 nen khong sao, nhung thu tu nay dung voi moi k.)
# O(n) voi dict. Do: n = 10^6 doc 0,12 s + vong 0,26-0,35 s (test 10^6 gia tri phan biet ca bai ~0,5 s: sat,
# nhung de nam 2023 cho phep Python va gioi han 1 giay).
# Subtask 2 (0 <= a[i] <= 10^6) co the dung mang dem thay dict - xem PAIRCOUNT_mang.py.
def main():
    data = open('PAIRCOUNT.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = map(int, data[2:2 + n])
    dem = {}
    lay = dem.get                 # gan ham vao bien cuc bo cho nhanh
    ans = 0
    for x in a:
        ans += lay(x - k, 0)      # so i < j co a[i] = a[j] - k
        dem[x] = lay(x, 0) + 1
    with open('PAIRCOUNT.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
