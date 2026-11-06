# TUILON - ban QHD theo khoi luong (giong TUI01). Dung, nhung bang W+1 o:
# qua subtask 2 (W <= 5*10^4); W = 10^9 thi het bo nho / qua gio.
def main():
    data = open('TUILON.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    if W > 10**7:                              # khong lap noi bang -> bo cuoc thay vi treo may
        with open('TUILON.OUT', 'w') as out:
            out.write('0\n')
        return
    f = [0] * (W + 1)
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        for s in range(W, w - 1, -1):
            x = f[s - w] + v
            if x > f[s]:
                f[s] = x
    with open('TUILON.OUT', 'w') as out:
        out.write(str(f[W]) + '\n')

main()
