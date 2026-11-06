# THAPHOP_sai - BAN SAI de chua bai: cung x lai sap y TANG -> hai hop cung canh nho (2,3), (2,5)
# bi dem thanh thap 2 tang. Dung 5/10 test (sai test 3, 5, 7, 9, 10: cac test co nhieu hop trung canh nho).
from bisect import bisect_left

def main():
    data = open('THAPHOP.INP', 'rb').read().split()
    n = int(data[0])
    v = list(map(int, data[1:1 + 2 * n]))
    p, q = v[0::2], v[1::2]
    # xoay: x = canh nho, y = canh lon; luu -y de sort tang theo (x, -y) = (x tang, y giam)
    hop = sorted(zip(map(min, p, q), map(max, p, q)))
    d = []
    for _, q in hop:
        y = q
        k = bisect_left(d, y)
        if k == len(d):
            d.append(y)
        else:
            d[k] = y
    with open('THAPHOP.OUT', 'w') as out:
        out.write(str(len(d)) + '\n')

main()
