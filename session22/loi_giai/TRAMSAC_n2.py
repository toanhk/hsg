# TRAMSAC - QHD O(n^2): voi moi i duyet lui j cho den khi x[i] - x[j] > L. Kip subtask 1-2 (n <= 5000).
# Voi n = 2*10^5 va L lon (cua so chua ca day) -> 2*10^10 phep, qua gio.
def main():
    data = open('TRAMSAC.INP', 'rb').read().split()
    n, L, P = int(data[0]), int(data[1]), int(data[2])
    x = [0] + [int(data[3 + 2 * i]) for i in range(n)]
    c = [0] + [int(data[4 + 2 * i]) for i in range(n)]
    INF = float('inf')
    f = [INF] * (n + 1); f[0] = 0
    for i in range(1, n + 1):
        best = INF
        j = i - 1
        while j >= 0 and x[i] - x[j] <= L:
            if f[j] < best:
                best = f[j]
            j -= 1
        f[i] = best + c[i]
    ans = min((f[j] for j in range(n + 1) if P - x[j] <= L), default=INF)
    with open('TRAMSAC.OUT', 'w') as fo:
        fo.write(str(ans if ans < INF else -1) + '\n')

main()
