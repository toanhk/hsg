# KETBAN - vet can: luu danh sach ke, moi cau hoi BFS tu u xem co toi v khong. O(q * (n + q)).
from collections import deque

def main():
    data = open('KETBAN.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    ke = [[] for _ in range(n + 1)]
    out = []
    for i in range(2, 2 + 3 * q, 3):
        t, u, v = int(data[i]), int(data[i + 1]), int(data[i + 2])
        if t == 1:
            ke[u].append(v); ke[v].append(u)
        else:
            tham = [False] * (n + 1)
            tham[u] = True
            dq = deque([u])
            while dq:
                x = dq.popleft()
                for y in ke[x]:
                    if not tham[y]:
                        tham[y] = True; dq.append(y)
            out.append('CO' if tham[v] else 'KHONG')
    with open('KETBAN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
