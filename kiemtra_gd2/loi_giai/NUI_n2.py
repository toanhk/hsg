# NUI - ban trung gian O(n^2): L[i] = 1 + max L[j] (j < i, h[j] < h[i]); R tuong tu.
# n = 2000: ~4*10^6 phep, kip. n = 2*10^5: 4*10^10 -> qua gio. Qua subtask 1, 2.
def main():
    data = open('NUI.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    L = [1] * n
    for i in range(n):
        hi = h[i]; b = 0
        for j in range(i):
            if h[j] < hi and L[j] > b: b = L[j]
        L[i] = b + 1
    R = [1] * n
    for i in range(n - 1, -1, -1):
        hi = h[i]; b = 0
        for j in range(i + 1, n):
            if h[j] < hi and R[j] > b: b = R[j]
        R[i] = b + 1
    with open('NUI.OUT', 'w') as f:
        f.write(str(n - max(L[i] + R[i] - 1 for i in range(n))) + '\n')

main()
