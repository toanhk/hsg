# THANHPHO - BFS dung list.pop(0) thay deque. Dung, nhung moi lan pop(0) Python dich ca mang
# sang trai -> O(n^2) khi hang doi dai. Qua subtask 1-2 (n <= 2000), cham o subtask 3.
def main():
    a = list(map(int, open('THANHPHO.INP', 'rb').read().split()))
    n, m, s, t = a[0], a[1], a[2], a[3]
    ke = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = a[4 + 2 * i], a[5 + 2 * i]
        ke[u].append(v); ke[v].append(u)
    dist = [-1] * (n + 1)
    dist[s] = 0
    q = [s]
    while q:
        u = q.pop(0)                           # <- O(do dai hang doi) moi lan
        for v in ke[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    with open('THANHPHO.OUT', 'w') as f:
        f.write(str(dist[t]) + '\n')

main()
