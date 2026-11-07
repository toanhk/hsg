# THU VIEN CODE MAU - QUY HOACH DONG (buoi 4-8, 17-20). Moi ham: trang thai ghi o docstring.
import bisect

def tui01(W, do_vat):
    """Cai tui 0/1 (buoi 6): do_vat = list (w, v). f[b] = gia tri lon nhat voi tong khoi luong <= b.
    Duyet b GIAM DAN de moi vat dung toi da 1 lan."""
    f = [0] * (W + 1)
    for w, v in do_vat:
        for b in range(W, w - 1, -1):
            if f[b - w] + v > f[b]:
                f[b] = f[b - w] + v
    return f[W]

def tui_vo_han(W, do_vat):
    """Cai tui khong gioi han so luong (buoi 6): duyet b TANG DAN."""
    f = [0] * (W + 1)
    for w, v in do_vat:
        for b in range(w, W + 1):
            if f[b - w] + v > f[b]:
                f[b] = f[b - w] + v
    return f[W]

def lis(a, tang_chat=True):
    """Do dai day con tang dai nhat O(n log n) (buoi 7). d[k] = gia tri cuoi nho nhat cua day tang dai k+1.
    tang_chat=False: day khong giam (dung bisect_right)."""
    d = []
    tim = bisect.bisect_left if tang_chat else bisect.bisect_right
    for x in a:
        i = tim(d, x)
        if i == len(d):
            d.append(x)
        else:
            d[i] = x
    return len(d)

def lcs(s, t):
    """Xau con chung dai nhat, giu 2 hang (buoi 7). f[j] = LCS(s[:i], t[:j])."""
    m = len(t)
    truoc = [0] * (m + 1)
    for ch in s:
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            if ch == t[j - 1]:
                cur[j] = truoc[j - 1] + 1
            else:
                cur[j] = cur[j - 1] if cur[j - 1] > truoc[j] else truoc[j]
        truoc = cur
    return truoc[m]

def sua_xau(s, t):
    """Khoang cach sua xau (chen/xoa/thay, buoi 7), 2 hang."""
    m = len(t)
    truoc = list(range(m + 1))
    for i, ch in enumerate(s, 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            cur[j] = truoc[j - 1] if ch == t[j - 1] else 1 + min(truoc[j - 1], truoc[j], cur[j - 1])
        truoc = cur
    return truoc[m]

def gop_da(a):
    """QHD tren doan (buoi 17): gop cac dong da canh nhau, chi phi moi lan = tong hai dong. n <= ~300.
    f[l][r] = chi phi nho nhat gop a[l..r] thanh 1 dong; tinh theo do dai doan tang dan."""
    n = len(a)
    s = [0] * (n + 1)
    for i, x in enumerate(a):
        s[i + 1] = s[i] + x
    f = [[0] * n for _ in range(n)]
    for d in range(2, n + 1):
        for l in range(n - d + 1):
            r = l + d - 1
            f[l][r] = min(f[l][k] + f[k + 1][r] for k in range(l, r)) + s[r + 1] - s[l]
    return f[0][n - 1] if n else 0

def tsp(d):
    """Nguoi giao hang qua moi diem roi ve 0 (bitmask, buoi 20), n <= 15. g[mask][v] = duong ngan nhat
    xuat phat 0, da tham tap mask, dang o v."""
    n = len(d)
    INF = float('inf')
    g = [[INF] * n for _ in range(1 << n)]
    g[1][0] = 0
    for mask in range(1, 1 << n):
        if not mask & 1:
            continue
        row = g[mask]
        for v in range(n):
            if row[v] == INF:
                continue
            for u in range(n):
                if not mask >> u & 1:
                    nv = row[v] + d[v][u]
                    if nv < g[mask | 1 << u][u]:
                        g[mask | 1 << u][u] = nv
    full = (1 << n) - 1
    return min(g[full][v] + d[v][0] for v in range(n)) if n > 1 else 0
