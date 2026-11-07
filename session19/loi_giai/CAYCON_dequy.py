# CAYCON - ban SAI de chua: DFS DE QUY dfs(u, cha).
# Dung tren cay ngau nhien (do sau nho), nhung cay "duong thang" 1-2-3-...-n co do sau n:
#   - khong tang gioi han: vo o do sau ~1000 (RecursionError);
#   - tang setrecursionlimit len lon: Python 3.11 tro xuong / Windows (stack 1 MB) thuong chet ca tien trinh
#     ma khong bao loi. Ban nay de 10000 nhu nhieu ban hay lam -> vo o cac test cay sau.
# Bai hoc: duyet cay trong phong thi phai bang vong lap (BFS lay thu tu roi duyet nguoc).
import sys
sys.setrecursionlimit(10000)

def main():
    data = open('CAYCON.INP', 'rb').read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        adj[u].append(v); adj[v].append(u)
    sz = [1] * (n + 1)

    def dfs(u, p):
        for v in adj[u]:
            if v != p:
                dfs(v, u)
                sz[u] += sz[v]

    dfs(1, 0)
    with open('CAYCON.OUT', 'w') as f:
        f.write(' '.join(map(str, sz[1:])) + '\n')

main()
