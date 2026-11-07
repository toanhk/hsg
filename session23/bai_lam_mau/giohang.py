# BAI LAM MAU CO LOI: ten file viet thuong (giohang.py), doc 'giohang.inp' -> Themis khong cham duoc.
def main():
    data = open('giohang.inp').read().split()
    with open('giohang.out', 'w') as f:
        f.write('0\n')

main()
