# LOTRINH - BFS dung, nhung truy vet bang DE QUY: in(v) goi in(cha[v]) truoc roi moi in v.
# Lo trinh dai hon ~1000 nut -> RecursionError (gioi han mac dinh cua Python la 1000 tang).
# Dung de chua bai: "khong de quy sau", truy vet bang vong lap + reverse.
from collections import deque

def main():
    a = list(map(int, open('LOTRINH.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        ke[a[2 + 2 * i]].append(a[3 + 2 * i])
    cha = [-1] * (n + 1)
    cha[1] = 0
    dist = [0] * (n + 1)
    q = deque([1])
    while q:
        u = q.popleft()
        for v in ke[u]:
            if cha[v] < 0:
                cha[v] = u; dist[v] = dist[u] + 1
                q.append(v)
    out = []

    def in_duong(v):
        if v == 0:
            return
        in_duong(cha[v])
        out.append(v)

    if cha[n] < 0:
        res = '-1\n'
    else:
        in_duong(n)
        res = f'{dist[n]}\n' + ' '.join(map(str, out)) + '\n'
    with open('LOTRINH.OUT', 'w') as f:
        f.write(res)

main()
