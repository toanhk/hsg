# XAUNP - vet can: duyet moi so 0 .. 2^n - 1, doi ra xau nhi phan n chu so, loai xau co '11'
# O(2^n * n): chi qua n <= 16 (n = 24 la 1,6*10^7 xau -> qua thoi gian)
def main():
    data = open('XAUNP.INP', 'rb').read().split()
    n = int(data[0])
    kq = []
    for m in range(1 << n):              # thu tu so tang dan = thu tu tu dien cua xau
        s = format(m, '0' + str(n) + 'b')
        if '11' not in s:
            kq.append(s)
    with open('XAUNP.OUT', 'w') as f:
        f.write(str(len(kq)) + '\n' + '\n'.join(kq) + '\n')

main()
