# DO THOI GIAN DOC/GHI TREN MAY PHONG THI
# Chay: python do_io.py   (lan dau mat vai giay de sinh file test)
# Moi cach chay 3 lan, lay thoi gian nho nhat. Khong tinh thoi gian khoi dong Python.
import random, sys, time

M = 10**6          # so dong canh "u v w"
TEN = 'CANH.INP'

def sinh_test():
    random.seed(2026)
    dong = [f'{random.randint(1, 10**5)} {random.randint(1, 10**5)} {random.randint(1, 10**9)}'
            for _ in range(M)]
    with open(TEN, 'w') as f:
        f.write(f'{10**5} {M}\n' + '\n'.join(dong) + '\n')

def doc_input():                      # Cach 1: input() tung dong
    sys.stdin = open(TEN)
    n, m = map(int, input().split())
    s = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        s += w
    return s

def doc_readline():                   # Cach 2: sys.stdin.readline tung dong
    sys.stdin = open(TEN)
    rl = sys.stdin.readline
    n, m = map(int, rl().split())
    s = 0
    for _ in range(m):
        u, v, w = map(int, rl().split())
        s += w
    return s

def doc_mot_lan():                    # Cach 3: doc toan bo mot lan, dung con tro
    data = open(TEN, 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    s = 0
    pos = 2
    for _ in range(m):
        u = int(data[pos]); v = int(data[pos + 1]); w = int(data[pos + 2])
        pos += 3
        s += w
    return s

KQ = [str(i) for i in range(10**6)]   # 10^6 dong can in

def ghi_print():                      # Ghi 1: print tung dong
    f = open('RA.OUT', 'w')
    for x in KQ:
        print(x, file=f)
    f.close()

def ghi_join():                       # Ghi 2: gom vao list, ghi mot lan
    with open('RA.OUT', 'w') as f:
        f.write('\n'.join(KQ) + '\n')

def vong_lap():                       # 10^7 phep cong don gian
    s = 0
    for i in range(10**7):
        s += i
    return s

def do(ham):
    tot = 1e9
    for _ in range(3):
        t = time.perf_counter()
        ham()
        tot = min(tot, time.perf_counter() - t)
    return tot

def main():
    sinh_test()
    print('Python', sys.version.split()[0], '| doc 10^6 dong "u v w", ghi 10^6 dong')
    for ham in (doc_input, doc_readline, doc_mot_lan, ghi_print, ghi_join, vong_lap):
        print(f'{ham.__name__:14s} {do(ham):6.2f} s')

main()
