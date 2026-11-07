# KPRIMESUB (Ninh Binh 2023-2024, ngay 06/10/2023, bai 2, 7 diem)
# Dem so doan con [L..R] cua [2..N] (2 <= L <= R <= N) chua it nhat K so nguyen to.
# T <= 100 bo test, N <= 10^5, 0 <= K <= 10^4.
# Y tuong: goi p[0] < p[1] < ... < p[c-1] la cac so nguyen to <= N.
#   Co dinh L. Neu so nguyen to dau tien >= L la p[i] thi doan [L..R] du K so nguyen to
#   <=> R >= p[i + K - 1]. So R hop le = N - p[i + K - 1] + 1 (neu i + K - 1 < c).
#   Moi L trong (p[i-1], p[i]] cung chung mot p[i] -> gop ca nhom: (p[i] - p[i-1]) * (N - p[i+K-1] + 1).
#   K = 0: moi doan deu thoa -> m(m+1)/2 voi m = N - 1.
# Sang Eratosthenes mot lan den 10^5; moi test O(pi(N)) ~ 9600 buoc -> T = 100 test ~ 10^6 buoc (do 0,15 s).
# Bay: chua sang lai cho moi test (100 lan sang 10^5 van kip nhung phi), quen truong hop K = 0,
#      K lon hon so nguyen to -> 0, va dap an vuot 2^31 (Python khong lo tran, C++/Pascal phai dung int64).
import bisect

def main():
    data = open('KPRIMESUB.INP', 'rb').read().split()
    t = int(data[0])
    q = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(t)]
    M = max(N for N, K in q)
    M = max(M, 2)
    sang = bytearray([1]) * (M + 1)
    sang[0] = sang[1] = 0
    for i in range(2, int(M ** 0.5) + 1):
        if sang[i]:
            sang[i * i::i] = bytes(len(range(i * i, M + 1, i)))
    p = [i for i in range(2, M + 1) if sang[i]]
    out = []
    for N, K in q:
        m = N - 1                                  # so phan tu cua [2..N]
        if K == 0:
            out.append(m * (m + 1) // 2)
            continue
        c = bisect.bisect_right(p, N)              # so nguyen to <= N
        ans = 0
        truoc = 1                                  # "p[-1]" = 1: L chay tu 2
        for i in range(c - K + 1):                 # can i + K - 1 <= c - 1
            ans += (p[i] - truoc) * (N - p[i + K - 1] + 1)
            truoc = p[i]
        out.append(ans)
    with open('KPRIMESUB.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
