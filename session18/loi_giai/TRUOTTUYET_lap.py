# TRUOTTUYET - ban CHAM "lap den khi on dinh": khong sap xep, cu quet ca luoi, cap nhat
# f[p] = 1 + max f[q] (q thap hon, ke p) cho den khi mot luot quet khong doi gi. Dung, nhung so luot quet
# co the bang do dai duong truot dai nhat L. Luoi hinh "ran" (duong truot di qua ca luoi) co L ~ r*c/2
# -> O((rc)^2): qua gio. Day la ly do phai tinh theo THU TU TO-PO (o day: do cao tang dan).
def main():
    data = open('TRUOTTUYET.INP', 'rb').read().split()
    r, c = int(data[0]), int(data[1])
    W = c + 2
    CAO = 1 << 40
    h = [CAO] * (W * (r + 2))
    p = 2
    for i in range(1, r + 1):
        base = i * W + 1
        h[base:base + c] = map(int, data[p:p + c])
        p += c
    o = [i * W + j for i in range(1, r + 1) for j in range(1, c + 1)]
    f = [1] * len(h)
    doi = True
    while doi:
        doi = False
        for x in o:
            hx = h[x]; best = f[x]
            for y in (x - W, x + W, x - 1, x + 1):
                if h[y] < hx and f[y] >= best:
                    best = f[y] + 1
            if best != f[x]:
                f[x] = best; doi = True
    with open('TRUOTTUYET.OUT', 'w') as fo:
        fo.write(str(max(f[x] for x in o)) + '\n')

main()
