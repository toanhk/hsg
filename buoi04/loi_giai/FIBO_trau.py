# FIBO - vet can: de quy thuan theo dinh nghia, KHONG nho
# So loi goi ~ 1.6^n: n = 30 mat ~0.1 s, n = 40 mat ~10 s, n = 50 khong bao gio xong
# Chi dung cho subtask 1 (T = 1, n <= 30). Khong lay mod vi F(30) = 832040 con nho.
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    data = open('FIBO.INP', 'rb').read().split()
    t = int(data[0])
    q = list(map(int, data[1:1 + t]))
    with open('FIBO.OUT', 'w') as f:
        f.write('\n'.join(str(fib(n) % (10**9 + 7)) for n in q) + '\n')

main()
