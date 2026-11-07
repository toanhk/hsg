# PHATUONG - BAN LOI "QUEN RESET" (de chua bai). Hoc sinh cap phat mang danh dau MOT LAN cho kich thuoc lon
# nhat roi dung lai cho moi bo test ma khong xoa -> o da tham o bo test truoc bi coi la da tham o bo sau.
# Bo test dau thuong DUNG, cac bo sau sai. Vi du cua de co 2 bo nen DA lo loi: luon chay thu vi du truoc khi nop!
# Bai hoc: bai nhieu bo test -> khoi tao lai MOI THU ben trong vong lap bo test (hoac dung mang moi).
from collections import deque

def main():
    data = open('PHATUONG.INP', 'rb').read().split()
    t = int(data[0]); pos = 1
    out = []
    MAX = 5 * 10**5 + 10
    da_tham = [[False, False] for _ in range(MAX)]      # cap phat MOT lan ...
    for _ in range(t):
        r, c = int(data[pos]), int(data[pos + 1]); pos += 2
        g = [data[pos + i].decode() for i in range(r)]; pos += r
        for i in range(r):
            for j in range(c):
                if g[i][j] == 'S': si, sj = i, j
                if g[i][j] == 'T': ti, tj = i, j
        # ... va QUEN dat lai da_tham = False o day
        q = deque([(si, sj, 0, 0)])
        da_tham[si * c + sj][0] = True
        ans = -1
        while q:
            i, j, k, d = q.popleft()
            if (i, j) == (ti, tj):
                ans = d; break
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < r and 0 <= b < c:
                    nk = k + (g[a][b] == '#')
                    if nk <= 1 and not da_tham[a * c + b][nk]:
                        da_tham[a * c + b][nk] = True
                        q.append((a, b, nk, d + 1))
        out.append(ans)
    with open('PHATUONG.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
