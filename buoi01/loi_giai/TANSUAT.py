# TANSUAT: n so, q truy van x -> so lan x xuat hien. n <= 10^6, q <= 2*10^5
from collections import Counter

def main():
    data = open('TANSUAT.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    dem = Counter(map(int, data[2:2 + n]))     # dem bang C, nhanh hon vong for + dict
    out = [str(dem[x]) for x in map(int, data[2 + n:2 + n + q])]   # Counter tra 0 neu khong co
    with open('TANSUAT.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
