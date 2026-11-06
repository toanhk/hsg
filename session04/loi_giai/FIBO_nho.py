# FIBO - co nho (memo, top-down): giong ban vet can nhung luu ket qua vao dict 'nho'
# Moi n chi tinh 1 lan -> O(n). Nhung de quy sau n tang:
#   - gioi han mac dinh 1000 tang -> n = 5000 bi RecursionError, phai setrecursionlimit
#   - lru_cache con te hon: Python 3.12+ gay loi o ~3000 tang du da setrecursionlimit
#   - n = 10^6 thi ngan xep qua sau, co the chet khong bao loi -> dung ban bang (FIBO.py)
# Qua subtask 1, 2 (n <= 5000).
import sys
MOD = 10**9 + 7

def main():
    sys.setrecursionlimit(20000)
    data = open('FIBO.INP', 'rb').read().split()
    t = int(data[0])
    q = list(map(int, data[1:1 + t]))
    nho = {0: 0, 1: 1}

    def fib(n):
        if n in nho:              # da tinh roi -> tra ngay, khong goi tiep
            return nho[n]
        r = (fib(n - 1) + fib(n - 2)) % MOD
        nho[n] = r
        return r

    with open('FIBO.OUT', 'w') as f:
        f.write('\n'.join(str(fib(n)) for n in q) + '\n')

main()
