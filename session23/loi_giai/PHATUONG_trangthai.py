# PHATUONG - BFS tren do thi trang thai (o, da pha chua) - DUNG nhung CHAM trong Python:
# tuple (i, j, k) + deque + kiem tra bien moi buoc, gap doi so trang thai. Test lon ~0,9 s tren may luyen tap
# (ban 2 BFS ~0,3 s): sat gio, may phong thi cham hon se mat diem subtask lon.
# (Buoi 14: do thi nhieu trang thai. O day co cach nhanh hon: 2 BFS tu S va T - xem PHATUONG.py.)
from collections import deque

def main():
    data = open('PHATUONG.INP', 'rb').read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in range(t):
        r, c = int(data[pos]), int(data[pos + 1]); pos += 2
        g = [data[pos + i].decode() for i in range(r)]; pos += r
        for i in range(r):
            for j in range(c):
                if g[i][j] == 'S': si, sj = i, j
                if g[i][j] == 'T': ti, tj = i, j
        d = [[[-1, -1] for _ in range(c)] for _ in range(r)]     # tao moi cho tung bo test
        d[si][sj][0] = 0
        q = deque([(si, sj, 0)])
        ans = -1
        while q:
            i, j, k = q.popleft()
            if (i, j) == (ti, tj):
                ans = d[i][j][k]; break
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < r and 0 <= b < c:
                    nk = k + (g[a][b] == '#')
                    if nk <= 1 and d[a][b][nk] == -1:
                        d[a][b][nk] = d[i][j][k] + 1
                        q.append((a, b, nk))
        out.append(ans)
    with open('PHATUONG.OUT', 'w') as f:
        f.write('\n'.join(map(str, out)) + '\n')

main()
