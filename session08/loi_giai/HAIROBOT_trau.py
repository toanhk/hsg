# HAIROBOT - vet can: liet ke moi duong (C(2n-2, n-1) duong), thu moi cap duong, tinh hop cac o.
# n = 6: 252 duong -> 63 504 cap; n = 8: 3432 duong -> 1.2*10^7 cap, qua cham. Chi subtask 1.
def main():
    data = open('HAIROBOT.INP', 'rb').read().split()
    n = int(data[0])
    a = [list(map(int, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
    ds = []                                        # moi duong la tap cac o (i*n + j)
    stack = [(0, 0, (0,))]
    while stack:                                   # duyet bang ngan xep, khong de quy
        i, j, o = stack.pop()
        if a[i][j] < 0:
            continue
        if i == n - 1 and j == n - 1:
            ds.append(set(o)); continue
        if i + 1 < n: stack.append((i + 1, j, o + ((i + 1) * n + j,)))
        if j + 1 < n: stack.append((i, j + 1, o + (i * n + j + 1,)))
    best = -1
    v = [a[x // n][x % n] for x in range(n * n)]
    tong = [sum(v[x] for x in p) for p in ds]
    for x in range(len(ds)):
        for y in range(x, len(ds)):
            t = tong[x] + tong[y] - sum(v[c] for c in ds[x] & ds[y])
            if t > best:
                best = t
    with open('HAIROBOT.OUT', 'w') as fo:
        fo.write(str(best) + '\n')

main()
