# BALO - ban cai tui quen thuoc (bang theo khoi luong): f[c] = gia tri lon nhat voi tai trong c,
# c duyet giam. Dung khi W <= 5*10^4 (subtask 1, 2); W = 10^9 thi khong tao noi mang -> 0 diem subtask 3.
def main():
    data = open('BALO.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    if W > 10**6:                       # tranh tao mang khong lo: bo subtask 3
        open('BALO.OUT', 'w').write('0\n')
        return
    f = [0] * (W + 1)
    for i in range(n):
        w, v = int(data[2 + 2 * i]), int(data[3 + 2 * i])
        for c in range(W, w - 1, -1):
            y = f[c - w] + v
            if y > f[c]:
                f[c] = y
    with open('BALO.OUT', 'w') as fo:
        fo.write(str(f[W]) + '\n')

main()
