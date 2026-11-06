# DUONGTD - vet can: quay lui moi duong don tu 1 den n, giu duong ngan nhat; bang do dai thi
# so sanh list (Python so sanh list theo tu dien). Chi subtask 1 (n <= 10).
import sys

def main():
    a = list(map(int, open('DUONGTD.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[2 + 2 * i], a[3 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    sys.setrecursionlimit(10000)
    best = [None]
    duong = [1]
    tham = [False] * (n + 1); tham[1] = True

    def thu(u):
        if u == n:
            b = best[0]
            if b is None or (len(duong), duong) < (len(b), b):
                best[0] = duong[:]
            return
        for v in ke[u]:
            if not tham[v]:
                tham[v] = True; duong.append(v)
                thu(v)
                tham[v] = False; duong.pop()

    thu(1)
    b = best[0]
    res = '-1\n' if b is None else f'{len(b) - 1}\n' + ' '.join(map(str, b)) + '\n'
    with open('DUONGTD.OUT', 'w') as f:
        f.write(res)

main()
