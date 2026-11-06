# DEMNGAN - SAI: gap lai dinh v da tham thi cong cnt[u] vao luon, khong kiem tra v co nam o tang
# NGAY SAU u khong. Canh noi hai dinh cung tang (tam giac) hoac canh ve tang truoc bi dem nham.
from collections import deque

MOD = 10**9 + 7

def main():
    a = list(map(int, open('DEMNGAN.INP', 'rb').read().split()))
    n, m = a[0], a[1]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[2 + 2 * i], a[3 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    dist = [-1] * (n + 1)
    cnt = [0] * (n + 1)
    dist[1] = 0; cnt[1] = 1
    q = deque([1])
    while q:
        u = q.popleft()
        for v in ke[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1; cnt[v] = cnt[u]; q.append(v)
            else:                              # <- thieu dieu kien dist[v] == dist[u] + 1
                cnt[v] = (cnt[v] + cnt[u]) % MOD
    with open('DEMNGAN.OUT', 'w') as f:
        f.write(f'{dist[n]} {cnt[n]}\n')

main()
