# LUALAN - BFS RIENG tu tung o 'F', thoi diem chay cua o = min qua cac nguon. Dung nhung
# O(k * m * n) voi k = so o F: rung 1000 x 1000 co 1000 dam chay -> 10^9 -> qua thoi gian.
# Dung de so sanh voi BFS nhieu nguon (LUALAN.py).
def main():
    data = open('LUALAN.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    vien = b'.' * W
    s = vien + b''.join(b'.' + r + b'.' for r in data[2:2 + m]) + vien
    VC = 10**9
    t = [VC] * len(s)
    nguon = [p for p in range(len(s)) if s[p] == 70]
    for goc in nguon:
        d = {goc: 0}
        tang = [goc]
        k = 0
        while tang:
            ke = []
            for p in tang:
                if k < t[p]:
                    t[p] = k
                for v in (p - W, p + W, p - 1, p + 1):
                    if s[v] == 84 and v not in d:
                        d[v] = k + 1
                        ke.append(v)
            tang = ke
            k += 1
    phut = 0
    con = 0
    for p in range(len(s)):
        if s[p] == 84:
            if t[p] == VC:
                con += 1
            elif t[p] > phut:
                phut = t[p]
    with open('LUALAN.OUT', 'w') as f:
        f.write(f'{phut} {con}\n')

main()
