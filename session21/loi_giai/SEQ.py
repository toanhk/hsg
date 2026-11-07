# SEQ (Ninh Binh 2023-2024, ngay 07/10/2023, bai 1, 7 diem) - bai ve nha buoi 21
# Q truy van K: doan con lien tiep dai nhat co moi phan tu <= K.  n, Q <= 10^5, |a[i]|, |K| <= 10^9.
# Y tuong (xu ly offline, giong DEMNHOM buoi 15): "bat" dan cac phan tu theo gia tri tang dan.
#   Khi bat a[i], doan sang chua i noi voi doan sang ben trai (ket thuc o i-1) va ben phai (bat dau o i+1).
#   Chi can luu do dai doan tai HAI DAU MUT: ln[dau] = ln[cuoi] = do dai -> moi lan bat O(1) (khong can DSU).
#   kq[c] = doan dai nhat sau khi bat c phan tu nho nhat.
#   Truy van K: c = so phan tu <= K = bisect_right(gia tri da sap, K) -> in kq[c].
# O((n + Q) log n): sap xep + bisect. Do ~0,2 s.
# Bay: K nho hon moi phan tu -> 0; gia tri bang nhau (bisect_right lay du ca nhom).
import bisect

def main():
    data = open('SEQ.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    ks = data[2 + n:2 + n + q]
    thu_tu = sorted(range(n), key=a.__getitem__)
    gt = [a[i] for i in thu_tu]
    ln = [0] * (n + 2)                 # chi so 1..n, hai dau 0 va n+1 luon "tat"
    kq = [0] * (n + 1)
    best = 0
    for c, i in enumerate(thu_tu, 1):
        i += 1
        trai = ln[i - 1]               # i-1 la dau cuoi cua doan ben trai (neu sang)
        phai = ln[i + 1]               # i+1 la dau trai cua doan ben phai
        dai = trai + phai + 1
        ln[i - trai] = dai
        ln[i + phai] = dai
        if dai > best:
            best = dai
        kq[c] = best
    out = [kq[bisect.bisect_right(gt, int(k))] for k in ks]
    with open('SEQ.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
