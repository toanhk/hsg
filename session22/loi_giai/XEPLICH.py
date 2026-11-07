# XEPLICH (de thi thu so 2, bai 3, 7 diem) - QHD mot chieu sau khi sap xep + bisect (buoi 5, 7)
# n cong viec, viec i lam tu ngay s[i] den ngay e[i] (ca hai dau), duoc p[i] dong. Mot nguoi khong lam hai viec
# trung nhau du chi mot ngay. Chon cac viec de tong tien lon nhat. n <= 2*10^5, 1 <= s <= e <= 10^9, p <= 10^9.
# QHD:
#   Sap xep viec theo ngay ket thuc tang dan: e[1] <= e[2] <= ... <= e[n].
#   Trang thai : f[i] = tong tien lon nhat chi dung i viec dau (theo thu tu da sap).
#   Cong thuc  : f[i] = max(f[i-1], p[i] + f[j]) voi j = so viec co e < s[i]   (bisect_left tren mang e).
#   Khoi tao   : f[0] = 0.
#   Thu tu     : i tang dan.     Dap an: f[n].
# O(n log n): sap xep + n lan bisect. Do ~0,3 s voi n = 2*10^5.
# Bay: tham lam "ket thuc som nhat" (dung khi moi p bang nhau, sai khi co trong so - XEPLICH_thamlam.py),
#      dieu kien trung ngay: viec ket thuc ngay 5 va viec bat dau ngay 5 la TRUNG (phai e < s, khong phai e <= s).
import bisect

def main():
    data = open('XEPLICH.INP', 'rb').read().split()
    n = int(data[0])
    s = list(map(int, data[1:1 + 3 * n:3]))
    e = list(map(int, data[2:2 + 3 * n:3]))
    p = list(map(int, data[3:3 + 3 * n:3]))
    od = sorted(range(n), key=e.__getitem__)                  # sap CHI SO theo ngay ket thuc (nhanh hon tuple)
    ends = [e[i] for i in od]
    tim = bisect.bisect_left
    f = [0] * (n + 1)
    cur = 0
    for i in range(n):
        k = od[i]
        b = p[k] + f[tim(ends, s[k], 0, i)]                    # so viec (trong i viec dau) co e < s
        if b > cur:
            cur = b
        f[i + 1] = cur
    with open('XEPLICH.OUT', 'w') as fo:
        fo.write(str(cur) + '\n')

main()
