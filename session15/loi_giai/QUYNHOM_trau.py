# QUYNHOM - vet can: luu tien tung nguoi; moi cau hoi "3 u" BFS tim ca nhom roi cong. O(q * (n + q)).
from collections import deque

def main():
    data = open('QUYNHOM.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    tien = [0] + list(map(int, data[2:2 + n]))
    pos = 2 + n
    ke = [[] for _ in range(n + 1)]
    out = []
    for _ in range(q):
        t = int(data[pos])
        if t == 1:
            u, v = int(data[pos + 1]), int(data[pos + 2]); pos += 3
            ke[u].append(v); ke[v].append(u)
        elif t == 2:
            tien[int(data[pos + 1])] += int(data[pos + 2]); pos += 3
        else:
            u = int(data[pos + 1]); pos += 2
            tham = [False] * (n + 1); tham[u] = True
            dq = deque([u]); s = 0
            while dq:
                x = dq.popleft(); s += tien[x]
                for y in ke[x]:
                    if not tham[y]:
                        tham[y] = True; dq.append(y)
            out.append(str(s))
    with open('QUYNHOM.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
