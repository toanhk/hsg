# HOANVI - vet can: sinh ca n! hoan vi bang itertools, bo trung bang set, sap xep
# n = 8: 40320 hoan vi (nhanh); n = 12: 4,8*10^8 hoan vi -> khong bao gio xong
from itertools import permutations

def main():
    data = open('HOANVI.INP', 'rb').read().split()
    s = data[0].decode()
    kq = sorted(set(''.join(p) for p in permutations(s)))
    with open('HOANVI.OUT', 'w') as f:
        f.write(str(len(kq)) + '\n' + '\n'.join(kq) + '\n')

main()
