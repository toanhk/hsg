# TUDIEN - vet can (<= 7 chu cai khac nhau): duyet moi hoan vi cac chu cai THEO THU TU TU DIEN,
# hoan vi dau tien lam day tu sap xep dung chinh la dap an.
from itertools import permutations

def main():
    data = open('TUDIEN.INP').read().split()
    n = int(data[0])
    w = data[1:1 + n]
    chu = sorted(set(''.join(w)))
    kq = '-1'
    for p in permutations(chu):
        hang = {c: i for i, c in enumerate(p)}
        khoa = [[hang[c] for c in x] for x in w]   # so sanh list Python = so sanh tu dien
        if all(khoa[i] <= khoa[i + 1] for i in range(n - 1)):
            kq = ''.join(p)
            break
    with open('TUDIEN.OUT', 'w') as f:
        f.write(kq + '\n')

main()
