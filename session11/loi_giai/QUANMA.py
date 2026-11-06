# QUANMA: ban co n x n, '.' o trong, '#' o co vat can (ma khong duoc DUNG o do, nhung duoc NHAY QUA).
# Quan ma o (x1,y1) can toi (x2,y2), moi nuoc di hinh chu L (2 theo mot chieu, 1 theo chieu kia).
# So nuoc it nhat? Khong toi duoc in -1. n <= 800
# BFS tren do thi "o -> 8 o ma nhay toi". Vien DAY 2 (vi ma nhay xa 2 o), W = n + 4,
# 8 huong thanh 8 do lech: +-2W+-1, +-W+-2. BFS theo tang, dung ngay khi toi dich.
# O(8 * n^2): 800 x 800 ~0.3 s; 1000 x 1000 ~0.45 s (xem do_loang.py) -> de cho n <= 800.
def main():
    data = open('QUANMA.INP', 'rb').read().split()
    n = int(data[0])
    x1, y1, x2, y2 = map(int, data[1:5])
    W = n + 4
    vien = b'#' * (2 * W)
    s = vien + b''.join(b'##' + r + b'##' for r in data[5:5 + n]) + vien
    dist = [-2 if c == 35 else -1 for c in s]
    S = (x1 + 1) * W + y1 + 1                # (x, y) tinh tu 1 -> p = (x-1+2)*W + (y-1+2)
    E = (x2 + 1) * W + y2 + 1
    huong = (-2 * W - 1, -2 * W + 1, -W - 2, -W + 2, W - 2, W + 2, 2 * W - 1, 2 * W + 1)
    dist[S] = 0
    tang = [S]
    d = 0
    while tang and dist[E] < 0:
        d += 1
        ke = []
        for p in tang:
            for h in huong:
                v = p + h
                if dist[v] == -1:
                    dist[v] = d
                    ke.append(v)
        tang = ke
    with open('QUANMA.OUT', 'w') as f:
        f.write(str(dist[E] if dist[E] >= 0 else -1) + '\n')

main()
