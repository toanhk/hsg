# BAI LAM MAU CO LOI: ten file viet thuong (muasam.py), doc 'muasam.inp' -> Themis khong cham duoc.
def main():
    data = open('muasam.inp').read().split()
    with open('muasam.out', 'w') as f:
        f.write('0\n')

main()
