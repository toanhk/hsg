# DEMXAU - vet can: duyet moi xau bang bitmask, kiem tra co k so 1 lien tiep khong
# O(2^n * n): chi qua subtask 1 (n <= 20).
def main():
    data = open('DEMXAU.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    xau_xau = '1' * k
    dem = 0
    for m in range(1 << n):
        if xau_xau not in format(m, 'b').zfill(n):
            dem += 1
    with open('DEMXAU.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
