# LOTRINH - vet can: quay lui moi duong di don tu 1, giu duong ngan nhat toi n.
# Chi subtask 1 (n <= 10).
import sys

def main():
    a = list(map(int, open('LOTRINH.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        ke[a[2 + 2 * i]].append(a[3 + 2 * i])
    sys.setrecursionlimit(10000)
    best = [None]
    duong = [1]
    tham = [False] * (n + 1)
    tham[1] = True

    def thu(u):
        if u == n:
            if best[0] is None or len(duong) < len(best[0]):
                best[0] = duong[:]
            return
        for v in ke[u]:
            if not tham[v]:
                tham[v] = True; duong.append(v)
                thu(v)
                tham[v] = False; duong.pop()

    thu(1)
    if best[0] is None:
        res = '-1\n'
    else:
        res = f'{len(best[0]) - 1}\n' + ' '.join(map(str, best[0])) + '\n'
    with open('LOTRINH.OUT', 'w') as f:
        f.write(res)

main()
