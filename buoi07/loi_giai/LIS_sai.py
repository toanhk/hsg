# LIS_sai - BAN SAI de chua bai: dung bisect_right thay bisect_left -> dem day KHONG GIAM
# (so bang nhau duoc noi tiep). Dung 5/10 test: sai o moi test co phan tu trung nhau (test 4, 6, 7, 9, 10).
from bisect import bisect_right

def main():
    data = open('LIS.INP', 'rb').read().split()
    n = int(data[0])
    a = map(int, data[1:1 + n])
    d = []
    for x in a:
        k = bisect_right(d, x)
        if k == len(d):
            d.append(x)
        else:
            d[k] = x
    with open('LIS.OUT', 'w') as out:
        out.write(str(len(d)) + '\n')

main()
