# DIENDAU - vet can: sinh moi cach dien bang itertools.product, ghep thanh xau roi eval
# 3^(n-1) bieu thuc, moi lan eval rat cham (~20 micro giay): chi qua n <= 8
from itertools import product

def main():
    data = open('DIENDAU.INP', 'rb').read().split()
    s = data[0].decode()
    S = int(data[1])
    dem = 0
    for dau in product(('', '+', '-'), repeat=len(s) - 1):
        bt = s[0] + ''.join(dau[i] + s[i + 1] for i in range(len(s) - 1))
        if eval(bt) == S:
            dem += 1
    with open('DIENDAU.OUT', 'w') as f:
        f.write(str(dem) + '\n')

main()
