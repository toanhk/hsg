# TENLUA - QHD O(n^2) cho ca hai cau (qua subtask 1, 2: n <= 3000)
#   f[i] = so qua nhieu nhat mot he thong chan duoc, ket thuc tai qua i: 1 + max f[j], j < i, h[j] >= h[i]
#   g[i] = day con tang chat dai nhat ket thuc tai i (Dilworth: cau 2 = max g)
def main():
    data = open('TENLUA.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    f = [1] * n
    g = [1] * n
    for i in range(n):
        hi = h[i]
        bf = bg = 0
        for j in range(i):
            hj = h[j]
            if hj >= hi:
                if f[j] > bf: bf = f[j]
            elif g[j] > bg:
                bg = g[j]
        f[i] = bf + 1
        g[i] = bg + 1
    with open('TENLUA.OUT', 'w') as out:
        out.write(f'{max(f)}\n{max(g)}\n')

main()
