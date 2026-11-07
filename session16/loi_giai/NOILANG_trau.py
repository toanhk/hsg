# NOILANG - vet can (n <= 8, m <= 12): thu moi tap n-1 canh, tap nao noi duoc moi lang thi lay tong.
# (Cay khung co dung n-1 canh; n-1 canh noi duoc n dinh <=> la cay.) Kiem tra lien thong bang BFS.
from itertools import combinations

def lien_thong(n, tap):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in tap:
        adj[u].append(v); adj[v].append(u)
    da = {1}; q = [1]
    for u in q:
        for v in adj[u]:
            if v not in da:
                da.add(v); q.append(v)
    return len(da) == n

def main():
    data = open('NOILANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(m)]
    best = -1
    for tap in combinations(canh, n - 1):
        if lien_thong(n, tap):
            t = sum(w for u, v, w in tap)
            if best < 0 or t < best:
                best = t
    with open('NOILANG.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
