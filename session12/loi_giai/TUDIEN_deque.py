# TUDIEN - ban SAI de chua: Kahn voi deque (khong phai heapq). Ra mot thu tu DUNG nhung khong chac la
# nho nhat theo tu dien, vi deque lay theo thu tu vao hang doi chu khong phai chu nho nhat.
from collections import deque

def main():
    data = open('TUDIEN.INP', 'rb').read().split()
    n = int(data[0])
    w = data[1:1 + n]
    co = [False] * 26
    for x in set(b''.join(w)):
        co[x - 97] = True
    ke = [set() for _ in range(26)]
    sai = False
    for i in range(n - 1):
        a, b = w[i], w[i + 1]
        for x, y in zip(a, b):
            if x != y:
                ke[x - 97].add(y - 97)
                break
        else:
            if len(a) > len(b):
                sai = True
                break
    out = '-1'
    if not sai:
        deg = [0] * 26
        for u in range(26):
            for v in ke[u]:
                deg[v] += 1
        q = deque(u for u in range(26) if co[u] and deg[u] == 0)
        kq = []
        while q:
            u = q.popleft(); kq.append(chr(97 + u))
            for v in sorted(ke[u]):
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        if len(kq) == sum(co):
            out = ''.join(kq)
    with open('TUDIEN.OUT', 'w') as f:
        f.write(out + '\n')

main()
