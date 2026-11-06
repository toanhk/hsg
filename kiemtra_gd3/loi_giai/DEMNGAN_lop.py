# DEMNGAN - ban trung gian: BFS lay d[] truoc, sau do voi MOI lop k quet lai TOAN BO cung de cong
# cnt cho lop k + 1. O(d[n] * m): dung voi subtask 2 (n, m <= 2000), cham khi duong ngan nhat dai.
MOD = 10**9 + 7
from collections import deque

def main():
    data = open('DEMNGAN.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    adj = [[] for _ in range(n + 1)]
    for u, v in canh:
        adj[u].append(v)
    d = [-1] * (n + 1); d[1] = 0; q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1; q.append(v)
    cnt = [0] * (n + 1); cnt[1] = 1
    for k in range(max(d[n], 0)):
        for u, v in canh:
            if d[u] == k and d[v] == k + 1:
                cnt[v] = (cnt[v] + cnt[u]) % MOD
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(f'{d[n]} {cnt[n]}\n' if d[n] >= 0 else '-1\n')

main()
