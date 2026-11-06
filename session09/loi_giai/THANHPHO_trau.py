# THANHPHO - vet can: quay lui moi duong di DON (khong lap dinh) tu s, ghi nhan duong ngan nhat
# toi t. So duong don bung no theo n -> chi subtask 1 (n <= 10).
import sys

def main():
    a = list(map(int, open('THANHPHO.INP', 'rb').read().split()))
    n, m, s, t = a[0], a[1], a[2], a[3]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[4 + 2 * i], a[5 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    sys.setrecursionlimit(10000)
    best = [-1]
    tham = [False] * (n + 1)

    def thu(u, d):
        if u == t:
            if best[0] < 0 or d < best[0]:
                best[0] = d
            return
        for v in ke[u]:
            if not tham[v]:
                tham[v] = True
                thu(v, d + 1)
                tham[v] = False

    tham[s] = True
    thu(s, 0)
    with open('THANHPHO.OUT', 'w') as f:
        f.write(str(best[0]) + '\n')

main()
