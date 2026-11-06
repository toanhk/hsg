# TRUYVET: cai tui 0/1 nhung phai in ra CAC VAT duoc chon. n <= 100, W <= 3*10^4
# Output: dong 1 gia tri lon nhat; dong 2 so vat k; dong 3 chi so cac vat (1..n, tang dan).
# Nhieu cach toi uu -> in cach nao cung duoc (cham bang kiem_tra.py).
#   QHD giong TUI01 (1 mang, s giam), them lay[i][s] = 1 neu khi xet vat i, o s duoc cap nhat
#   (tuc la phuong an tot nhat cho (i vat dau, s) CO lay vat i).
#   Truy vet: di nguoc i = n..1, s = W: neu lay[i][s] thi chon vat i va s -= w[i].
# Bo nho lay: n bytearray (W+1) byte = 3*10^6 byte ~ 3 MB (list so nguyen se ~ 24 MB).
def main():
    data = open('TRUYVET.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    w = [0] * (n + 1)
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i], v[i] = int(data[2 * i]), int(data[2 * i + 1])
    f = [0] * (W + 1)
    lay = [None] * (n + 1)
    for i in range(1, n + 1):
        wi, vi = w[i], v[i]
        c = bytearray(W + 1)
        for s in range(W, wi - 1, -1):
            x = f[s - wi] + vi
            if x > f[s]:
                f[s] = x
                c[s] = 1
        lay[i] = c
    chon = []
    s = W
    for i in range(n, 0, -1):                  # truy vet tu vat cuoi ve vat dau
        if lay[i][s]:
            chon.append(i)
            s -= w[i]
    chon.reverse()
    with open('TRUYVET.OUT', 'w') as out:
        out.write(f'{f[W]}\n{len(chon)}\n' + ' '.join(map(str, chon)) + '\n')

main()
