# TONG: tinh tong n so va dem so chan. n <= 10^6
def main():
    data = open('TONG.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))     # chuyen ca doan mot lan
    tong = sum(a)
    chan = sum(1 for x in a if x % 2 == 0)
    with open('TONG.OUT', 'w') as f:
        f.write(f'{tong}\n{chan}\n')

main()
