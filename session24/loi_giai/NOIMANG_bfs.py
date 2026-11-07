# NOIMANG - cach thu hai (cung dung tron diem): BFS tu moi may chua tham, dem cum va kich thuoc. O(n + m).
from collections import deque

def main():
    data = open('NOIMANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for k in range(m):
        u, v = int(data[2 + 2 * k]), int(data[3 + 2 * k])
        adj[u].append(v); adj[v].append(u)
    seen = [False] * (n + 1); cum = 0; lon = 0
    for s in range(1, n + 1):
        if seen[s]:
            continue
        cum += 1; seen[s] = True; q = deque([s]); dem = 0
        while q:
            u = q.popleft(); dem += 1
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True; q.append(v)
        lon = max(lon, dem)
    with open('NOIMANG.OUT', 'w') as f:
        f.write(f'{cum - 1}\n{lon}\n')

main()
