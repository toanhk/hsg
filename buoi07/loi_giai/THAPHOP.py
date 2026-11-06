# THAPHOP: n hop chu nhat (day) kich thuoc a_i x b_i, duoc XOAY 90 do. Hop X dat len hop Y neu ca hai
# canh cua X nho hon HAN hai canh cua Y (sau khi xoay hop ly). Thap cao nhat gom bao nhieu hop?
# n <= 2*10^5, kich thuoc <= 10^9
# Buoc 1: xoay moi hop cho canh nho truoc (x <= y). X dat len Y <=> x_X < x_Y va y_X < y_Y.
#   (neu dat duoc theo cach xoay nao do thi dat duoc theo cach "nho voi nho, lon voi lon")
# Buoc 2: sap theo x TANG, cung x thi y GIAM. Thap = day con TANG CHAT cua cac y.
#   Vi sao y giam khi cung x? Hai hop cung x khong chong len nhau duoc; y giam bao dam LIS tang chat
#   tren y khong lay duoc 2 hop cung x. (Neu sap y tang, (2,3) va (2,5) bi tinh nham thanh 2 tang.)
# Buoc 3: LIS bang bisect_left. Tong O(n log n) ~ 0.3 s (sort + bisect)
# (Sap theo cap (x, -y) cung dung, nhung sort tuple cham hon sort so nguyen ~2 lan.)
from bisect import bisect_left

def main():
    data = open('THAPHOP.INP', 'rb').read().split()
    n = int(data[0])
    v = list(map(int, data[1:1 + 2 * n]))
    p, q = v[0::2], v[1::2]
    # xoay: x = canh nho, y = canh lon. Sap theo (x tang, y giam) bang MOT so nguyen:
    #   khoa = x * 2^31 + (2^30 - y)  (y <= 10^9 < 2^30) -> sort so nguyen nhanh hon sort cap (x, -y)
    G = 1 << 30
    khoa = sorted([(x << 31) | (G - y) for x, y in zip(map(min, p, q), map(max, p, q))])
    M = (1 << 31) - 1
    d = []
    for k in khoa:
        y = G - (k & M)
        i = bisect_left(d, y)
        if i == len(d):
            d.append(y)
        else:
            d[i] = y
    with open('THAPHOP.OUT', 'w') as out:
        out.write(str(len(d)) + '\n')

main()
