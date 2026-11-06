# MAKHOA - khong dung BFS: lap "noi long" kieu Bellman-Ford. Ban dau d[S] = 0, cac ma khac vo cung;
# moi luot duyet moi ma x, moi ma ke y: d[y] = min(d[y], d[x] + 1). Lap toi khi khong doi.
# Moi luot O(10^n * 2n), so luot toi da 10^n -> chi subtask 1 (n <= 2).
def main():
    data = open('MAKHOA.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    S, T = int(data[2]), int(data[3])
    N = 10**n
    cam = set(int(x) for x in data[4:4 + k])
    INF = 10**9
    d = [INF] * N
    d[S] = 0

    def ke(x):
        s = str(x).zfill(n)
        for i in range(n):
            c = int(s[i])
            for c2 in ((c + 1) % 10, (c - 1) % 10):
                yield int(s[:i] + str(c2) + s[i + 1:])

    doi = True
    while doi:
        doi = False
        for x in range(N):
            if d[x] == INF or x in cam:
                continue
            for y in ke(x):
                if y not in cam and d[x] + 1 < d[y]:
                    d[y] = d[x] + 1; doi = True
    res = -1 if d[T] == INF or T in cam else d[T]
    with open('MAKHOA.OUT', 'w') as f:
        f.write(str(res) + '\n')

main()
