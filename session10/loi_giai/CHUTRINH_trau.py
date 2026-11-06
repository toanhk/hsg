# CHUTRINH - vet can: canh (u, v) nam tren mot chu trinh <=> bo canh do di, u van den duoc v.
# Thanh phan co chu trinh <=> co it nhat mot canh nam tren chu trinh.
# Voi moi canh: bo no, BFS tu u xem co den v khong -> O(m * (n + m)): chi subtask 1 (n, m <= 1000).
from collections import deque

def main():
    data = open('CHUTRINH.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    ke = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(canh):
        ke[u].append((v, i))
        ke[v].append((u, i))

    tren_chu_trinh = [False] * (n + 1)         # dinh u la dau mut cua mot canh tren chu trinh
    for i, (u, v) in enumerate(canh):
        tham = [False] * (n + 1)
        tham[u] = True
        q = deque([u])
        while q:
            x = q.popleft()
            for y, j in ke[x]:
                if j != i and not tham[y]:
                    tham[y] = True
                    q.append(y)
        if tham[v]:
            tren_chu_trinh[u] = True

    # dem thanh phan chua it nhat mot dinh danh dau
    tham = [False] * (n + 1)
    dem = 0
    for s in range(1, n + 1):
        if tham[s]:
            continue
        tham[s] = True
        q = deque([s])
        co = False
        while q:
            x = q.popleft()
            co = co or tren_chu_trinh[x]
            for y, _ in ke[x]:
                if not tham[y]:
                    tham[y] = True
                    q.append(y)
        dem += co
    with open('CHUTRINH.OUT', 'w') as out:
        out.write(str(dem) + '\n')

main()
