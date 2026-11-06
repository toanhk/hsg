# VE1 - vet can: de quy thu ca 3 thao tac, KHONG nho.
# Cung mot so bi tinh lai rat nhieu lan -> chi qua subtask 1 (n <= 100).
import sys

def f(n):
    if n == 1:
        return 0
    b = f(n - 1)
    if n % 2 == 0:
        b = min(b, f(n // 2))
    if n % 3 == 0:
        b = min(b, f(n // 3))
    return b + 1

def main():
    sys.setrecursionlimit(10000)
    data = open('VE1.INP', 'rb').read().split()
    t = int(data[0])
    with open('VE1.OUT', 'w') as out:
        out.write('\n'.join(str(f(int(x))) for x in data[1:1 + t]) + '\n')

main()
