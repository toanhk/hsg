# BAI LAM MAU CO LOI HINH THUC (de chay thu soat_bai.py): doc ban phim, de quy, khong ghi file.
import sys
sys.setrecursionlimit(10**6)

def dem(a, i, X, s):              # de quy: dem doan bat dau tu i
    if i == len(a) or s + a[i] > X:
        return 0
    return 1 + dem(a, i + 1, X, s + a[i])

n, L, R = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for l in range(n):
    ans += dem(a, l, R, 0) - dem(a, l, L - 1, 0)
print(ans)
