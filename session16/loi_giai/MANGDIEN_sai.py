# MANGDIEN - ban SAI de chua (tham lam "1 tram"): xay MOT tram o lang re nhat + cay khung cac day.
# Sai 2 cho: (1) do thi day co the KHONG lien thong -> moi thanh phan can mot tram rieng;
# (2) ke ca khi lien thong, xay them tram co the re hon keo mot day dat (vi du day 100, tram 5).
def main():
    data = open('MANGDIEN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + n]))
    p = 2 + n
    canh = sorted((int(data[i + 2]), int(data[i]), int(data[i + 1])) for i in range(p, p + 3 * m, 3))
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    tong = min(c)
    for w, u, v in canh:
        a = find(u); b = find(v)
        if a != b:
            parent[a] = b; tong += w
    with open('MANGDIEN.OUT', 'w') as f:
        f.write(str(tong) + '\n')

main()
