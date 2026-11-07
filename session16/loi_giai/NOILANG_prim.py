# NOILANG - Prim voi heapq (gioi thieu). Moc cay tu lang 1: moi buoc lay canh RE NHAT noi cay voi mot
# lang chua vao cay. Giong Dijkstra, chi khac khoa trong heap la w (khong phai d + w).
# Dung, nhung moi canh co the vao heap 2 lan -> ~0,7 s voi m = 2*10^5 (gap 2,5 lan Kruskal).
# Nen dung Prim khi do thi DAY va cho bang ma tran (xem PHANCUM o de kiem tra giai doan 4).
import heapq

def main():
    data = open('NOILANG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        adj[u].append((w, v)); adj[v].append((w, u))
    vao = [False] * (n + 1)                    # vao[u] = lang u da nam trong cay
    pq = [(0, 1)]
    tong = 0; dem = 0
    while pq:
        w, u = heapq.heappop(pq)
        if vao[u]:
            continue                           # ban ghi loi thoi (u da vao cay bang canh re hon)
        vao[u] = True; tong += w; dem += 1
        for e in adj[u]:
            if not vao[e[1]]:
                heapq.heappush(pq, e)
    with open('NOILANG.OUT', 'w') as f:
        f.write(str(tong if dem == n else -1) + '\n')

main()
