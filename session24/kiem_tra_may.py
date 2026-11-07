# KIEM TRA MAY / MOI TRUONG PYTHON truoc ngay thi (buoi 24). Chay tren CHINH may luyen tap va (neu duoc phep)
# tren may phong thi hoac may cung cau hinh:   python kiem_tra_may.py
# In ra: phien ban Python (CPython hay PyPy), cac module can dung, kha nang doc/ghi file .INP/.OUT trong thu
# muc hien tai, gioi han de quy, va DO TOC DO 6 phep chuan, so voi so do tren may soan bai (cloud Linux,
# Python 3.13) de ra HE SO CHAM. Ket qua cung ghi vao kiem_tra_may.txt de giao vien thu lai.
# Cach dung he so: neu he so = 1,8 thi bai nao loi giai mau do 0,4 s se mat ~0,7 s tren may nay; lay
# "10^7 phep / giay" chia cho he so de uoc luong lai gioi han n cho Python.
import os, platform, subprocess, sys, tempfile, time

# So do tham chieu tren may soan bai (giay) - lay tu do_io.py, do_ctdl.py, do_bfs.py cac buoi truoc.
THAM_CHIEU = {
    '10^7 phep cong trong main()': 0.30,
    'doc 10^6 so bang read().split()': 0.12,
    'sort 10^6 so nguyen': 0.25,
    'heappush + heappop 10^6 lan': 1.20,
    'BFS deque 2*10^5 dinh / 4*10^5 canh': 0.20,
    'ghi 10^6 dong bang join': 0.10,
}

dong = []

def in_ra(s=''):
    print(s)
    dong.append(s)

def do(ten, ham):
    t = time.perf_counter()
    ham()
    tg = time.perf_counter() - t
    hs = tg / THAM_CHIEU[ten]
    in_ra(f'  {ten:40s} {tg:6.2f} s   (may soan bai {THAM_CHIEU[ten]:.2f} s, he so {hs:.2f})')
    return hs

def cong():
    s = 0
    for i in range(10**7):
        s += i
    return s

def main():
    in_ra('=== THONG TIN PYTHON')
    in_ra(f'  Phien ban : {sys.version.split()[0]} ({platform.python_implementation()})')
    in_ra(f'  He dieu hanh: {platform.system()} {platform.release()}  |  may: {platform.machine()}')
    in_ra(f'  Duong dan : {sys.executable}')
    if sys.version_info < (3, 8):
        in_ra('  [CANH BAO] Python < 3.8: mot so cu phap (f-string "=", :=, math.comb) khong co.')
    if platform.python_implementation() == 'PyPy':
        in_ra('  [GHI CHU] Day la PyPy: vong lap nhanh hon 5-20 lan, nhung de quy va list lon ton bo nho hon.')

    in_ra('\n=== MODULE THUONG DUNG')
    for m in ('collections', 'heapq', 'bisect', 'itertools', 'functools', 'math', 'array'):
        try:
            __import__(m); in_ra(f'  {m:12s} co')
        except ImportError:
            in_ra(f'  {m:12s} KHONG CO  <-- bao giam thi / doi cach viet')
    try:
        from math import comb, isqrt  # noqa: F401
        in_ra('  math.comb, math.isqrt   co (Python >= 3.8)')
    except ImportError:
        in_ra('  math.comb/isqrt KHONG CO -> tu viet to hop / can bac hai nguyen')

    in_ra('\n=== DOC / GHI FILE TRONG THU MUC HIEN TAI')
    try:
        with open('THUMAY.INP', 'w') as f:
            f.write('3\n1 2 3\n')
        data = open('THUMAY.INP', 'rb').read().split()
        with open('THUMAY.OUT', 'w') as f:
            f.write(str(sum(map(int, data[1:]))) + '\n')
        ok = open('THUMAY.OUT').read().strip() == '6'
        os.remove('THUMAY.INP'); os.remove('THUMAY.OUT')
        in_ra(f'  Ghi/doc THUMAY.INP -> THUMAY.OUT: {"OK" if ok else "SAI"}  (thu muc: {os.getcwd()})')
    except OSError as e:
        in_ra(f'  [LOI] Khong ghi duoc file trong thu muc nay: {e}')

    in_ra('\n=== DE QUY (chay trong tien trinh con de khong lam treo chuong trinh nay)')
    for sau in (10**4, 10**5, 5 * 10**5):
        code = ('import sys\nsys.setrecursionlimit(10**6)\n'
                'def f(n):\n    return 0 if n == 0 else 1 + f(n - 1)\n'
                f'print(f({sau}))\n')
        try:
            r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=20)
            ok = r.returncode == 0 and r.stdout.strip() == str(sau)
        except subprocess.TimeoutExpired:
            ok = False
        in_ra(f'  De quy sau {sau:>7}: {"chay duoc" if ok else "VO (tran ngan xep / RecursionError)"}')
    in_ra('  -> Du chay duoc, trong bai thi van viet DFS / duyet cay / find bang VONG LAP.')

    in_ra('\n=== TOC DO (so voi may soan bai)')
    import heapq
    from collections import deque
    import random
    random.seed(1)
    hs = []
    hs.append(do('10^7 phep cong trong main()', cong))
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, 'A.INP')
        with open(p, 'w') as f:
            f.write(' '.join(str(random.randint(1, 10**9)) for _ in range(10**6)))
        hs.append(do('doc 10^6 so bang read().split()', lambda: list(map(int, open(p, 'rb').read().split()))))
        a = [random.randint(1, 10**9) for _ in range(10**6)]
        hs.append(do('sort 10^6 so nguyen', lambda: sorted(a)))

        def heap():
            h = []
            for x in a:
                heapq.heappush(h, x)
            for _ in range(len(a)):
                heapq.heappop(h)
        hs.append(do('heappush + heappop 10^6 lan', heap))
        n, m = 2 * 10**5, 4 * 10**5
        adj = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            j = random.randint(1, i - 1); adj[i].append(j); adj[j].append(i)
        for _ in range(m - n + 1):
            u, v = random.randint(1, n), random.randint(1, n); adj[u].append(v); adj[v].append(u)

        def bfs():
            d = [-1] * (n + 1); d[1] = 0; q = deque([1])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if d[v] < 0:
                        d[v] = d[u] + 1; q.append(v)
        hs.append(do('BFS deque 2*10^5 dinh / 4*10^5 canh', bfs))
        out = os.path.join(tmp, 'A.OUT')

        def ghi():
            with open(out, 'w') as f:
                f.write('\n'.join(map(str, a)) + '\n')
        hs.append(do('ghi 10^6 dong bang join', ghi))
    tb = sorted(hs)[len(hs) // 2]
    in_ra(f'\n  HE SO CHAM (trung vi): {tb:.2f}')
    if tb <= 1.2:
        in_ra('  May nay nhanh ngang may soan bai: cac loi giai mau (<= 0,4 s) con du thoi gian.')
    elif tb <= 2.0:
        in_ra('  May cham hon. Bai nao loi giai cua em do > 0,5 s o nha thi can toi uu them (buoi 23).')
    else:
        in_ra('  May CHAM NHIEU. Uoc luong lai: Python chi ~' + f'{10**7 / tb:.1e}' +
              ' phep/giay; uu tien subtask, tranh hang so lon.')
    with open('kiem_tra_may.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(dong) + '\n')
    print('\nDa ghi ket qua vao kiem_tra_may.txt')

main()
