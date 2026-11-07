# DONGHANG - ban SAI de chua (tham lam): xep kien len xe hien tai cho den khi day (K kien hoac vuot W).
# Sai vi dung it xe chua chac re: vi du K = 2, a = 1 9 9 1 -> tham lam (1 9)(9 1) = 18, toi uu (1)(9 9)(1) = 11.
def main():
    data = open('DONGHANG.INP', 'rb').read().split()
    n, K, W = int(data[0]), int(data[1]), int(data[2])
    a = list(map(int, data[3:3 + n]))
    tong = 0; dem = 0; s = 0; mx = 0
    for x in a:
        if dem == K or s + x > W:
            tong += mx; dem = 0; s = 0; mx = 0
        dem += 1; s += x; mx = max(mx, x)
    tong += mx
    with open('DONGHANG.OUT', 'w') as f:
        f.write(str(tong) + '\n')

main()
