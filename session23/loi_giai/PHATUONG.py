# PHATUONG (de thi thu so 3, bai 3, 7 diem) - nhieu bo test, BFS tu hai dau (buoi 9, 11)
# T bo test. Moi bo: luoi r x c gom '.', '#', 'S', 'T'. Moi buoc sang o ke canh (4 huong).
# Duoc PHA TOI DA MOT o tuong '#': buoc vao o do tinh nhu mot buoc thuong. So buoc it nhat tu S den T (-1 neu khong).
# T <= 10^4, tong r*c tren moi bo test <= 5*10^5.
# Y tuong: BFS tu S (dS) va BFS tu T (dT) chi tren o trong.
#   Khong pha: dS[T]. Pha o tuong w: (min dS cua o ke w) + 1 (vao w) + 1 (ra khoi w) + (min dT cua o ke w).
#   -> 2 BFS + 1 lan quet tuong, O(r*c) moi bo test.
# Cai dat (buoi 11): luoi co VIEN (o vien la 'X', khong pha duoc), o (i, j) ma hoa p = (i+1)*W + (j+1),
#   BFS theo tang bang list. Do: tong r*c = 5*10^5 ca bai ~0,35 s.
# Bay (de nay de bat loi): QUEN RESET mang danh dau giua cac bo test (PHATUONG_quenreset.py),
#   BFS trang thai (o, da pha chua) bang tuple + deque dung nhung cham (PHATUONG_trangthai.py),
#   khong co duong va khong co tuong -> -1, S ke T, pha tuong o vien ban do (khong duoc: ngoai ban do).
def main():
    data = open('PHATUONG.INP', 'rb').read().split()
    t = int(data[0]); pos = 1
    out = []
    TUONG, VIEN = ord('#'), ord('X')
    for _ in range(t):
        r, c = int(data[pos]), int(data[pos + 1]); pos += 2
        W = c + 2
        g = bytearray(b'X' * W)                 # hang vien tren
        for i in range(r):
            g += b'X' + data[pos + i] + b'X'
        g += b'X' * W                           # hang vien duoi
        pos += r
        s, e = g.find(b'S'), g.find(b'T')
        N = len(g)
        BIG = 1 << 30

        def bfs(src):                           # BFS theo tang tren o trong ('.', 'S', 'T')
            d = [BIG] * N
            d[src] = 0
            tang = [src]; k = 0
            while tang:
                k += 1
                moi = []
                for p in tang:
                    for q in (p - 1, p + 1, p - W, p + W):
                        if d[q] == BIG and g[q] != TUONG and g[q] != VIEN:
                            d[q] = k
                            moi.append(q)
                tang = moi
            return d

        dS = bfs(s); dT = bfs(e)                # mang moi cho MOI bo test -> khong the quen reset
        best = dS[e]
        p = g.find(TUONG)
        while p != -1:                          # duyet cac o tuong
            a = min(dS[p - 1], dS[p + 1], dS[p - W], dS[p + W])
            if a < BIG:
                b = min(dT[p - 1], dT[p + 1], dT[p - W], dT[p + W])
                if a + b + 2 < best:
                    best = a + b + 2
            p = g.find(TUONG, p + 1)
        out.append(best if best < BIG else -1)
    with open('PHATUONG.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
