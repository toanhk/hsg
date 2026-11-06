# HAIROBOT - ban SAI de chua bai (tham lam hai lan): cho robot 1 di duong nhieu vang nhat
# (bai VANG), xoa vang tren duong do, roi cho robot 2 di duong nhieu vang nhat tren bang con lai.
# Moi robot toi uu rieng KHONG cho tong toi uu: robot 1 "an" mat o ma robot 2 can.
def toi_uu(a, n):                                  # tra ve (tong, danh sach o) cua duong tot nhat
    AM = -1
    f = [[AM] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] < 0:
                continue
            if i == 0 and j == 0:
                f[i][j] = a[i][j]; continue
            b = max(f[i - 1][j] if i else AM, f[i][j - 1] if j else AM)
            if b >= 0:
                f[i][j] = b + a[i][j]
    if f[n - 1][n - 1] < 0:
        return AM, []
    o = [(n - 1, n - 1)]
    i = j = n - 1
    while i or j:
        if i and f[i - 1][j] == f[i][j] - a[i][j]:
            i -= 1
        else:
            j -= 1
        o.append((i, j))
    return f[n - 1][n - 1], o

def main():
    data = open('HAIROBOT.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    t1, o = toi_uu(a, n)
    if t1 < 0:
        kq = -1
    else:
        for i, j in o:
            a[i][j] = 0
        t2, _ = toi_uu(a, n)
        kq = t1 + t2
    with open('HAIROBOT.OUT', 'w') as fo:
        fo.write(str(kq) + '\n')

main()
