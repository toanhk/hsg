# TUI01 - ban SAI de chua bai: duyet s TANG dan tren 1 mang
# -> f[s - w] co the da chua chinh vat nay, nen mot vat bi lay nhieu lan.
# Vi du: n = 1, W = 10, vat (3, 5): dung la 5, ban nay ra 15 (lay 3 lan).
def main():
    data = open('TUI01.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    f = [0] * (W + 1)
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        for s in range(w, W + 1):              # SAI: phai la range(W, w - 1, -1)
            x = f[s - w] + v
            if x > f[s]:
                f[s] = x
    with open('TUI01.OUT', 'w') as out:
        out.write(str(f[W]) + '\n')

main()
