# THAPHOP - QHD O(n^2) (qua subtask 1, 2: n <= 3000): sau khi xoay va sap theo x tang,
#   f[i] = so hop nhieu nhat cua thap co hop i o DAY (to nhat): 1 + max f[j], x_j < x_i va y_j < y_i
#   Day la QHD tren DAG "hop j dat duoc len hop i" -- se gap lai o buoi 18.
def main():
    data = open('THAPHOP.INP', 'rb').read().split()
    n = int(data[0])
    hop = []
    for i in range(n):
        p, q = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        hop.append((min(p, q), max(p, q)))
    hop.sort()
    f = [1] * n
    for i in range(n):
        xi, yi = hop[i]
        tot = 0
        for j in range(i):
            xj, yj = hop[j]
            if xj < xi and yj < yi and f[j] > tot:
                tot = f[j]
        f[i] = tot + 1
    with open('THAPHOP.OUT', 'w') as out:
        out.write(str(max(f)) + '\n')

main()
