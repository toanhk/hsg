# MONHOC - ban trung gian O(n * (n + m)): moi luot QUET LAI moi mon tim mon chua hoc co deg = 0.
# Dung voi subtask 2 (n <= 1000), qua thoi gian voi n = 2*10^5 (de chua bai: vi sao can hang doi).
def main():
    data = open('MONHOC.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i]); v = int(data[i + 1])
        adj[u].append(v); deg[v] += 1
    hoc = [False] * (n + 1)
    thu_tu = []
    for _ in range(n):
        u = 1
        while u <= n and (hoc[u] or deg[u]):   # quet tim mon hoc duoc
            u += 1
        if u > n:
            break                               # khong con mon nao hoc duoc -> co chu trinh
        hoc[u] = True; thu_tu.append(u)
        for v in adj[u]:
            deg[v] -= 1
    with open('MONHOC.OUT', 'w') as f:
        f.write((' '.join(map(str, thu_tu)) if len(thu_tu) == n else '-1') + '\n')

main()
