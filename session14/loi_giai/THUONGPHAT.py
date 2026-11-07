# THUONGPHAT: n o, m loi di MOT CHIEU u -> v, di qua ton w diem (w < 0 nghia la duoc THUONG |w| diem).
# Tim tong diem it nhat de di tu 1 den n. In KHONG neu khong toi duoc, VOCUC neu co the nho tuy y
# (co chu trinh am nam tren mot duong 1 ~~> n). n <= 1000, m <= 5000, |w| <= 10^4.
# Dijkstra SAI khi co canh am -> Bellman-Ford:
#   1) Lap toi da n - 1 vong, moi vong noi long MOI canh; dung som neu mot vong khong doi gi.
#      (duong ngan nhat khong lap dinh co <= n - 1 canh, vong thu i chac chan chot xong duong i canh)
#   2) Chay them vong thu n: dinh nao VAN giam duoc thi nam tren / sau mot chu trinh am toi duoc tu 1.
#   3) Loang (BFS) tu cac dinh do theo chieu canh: neu cham n -> VOCUC.
# O(n * m) = 5*10^6 truong hop xau nhat.
from collections import deque

def main():
    data = open('THUONGPHAT.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = []
    adj = [[] for _ in range(n + 1)]
    for i in range(2, 2 + 3 * m, 3):
        u = int(data[i]); v = int(data[i + 1]); w = int(data[i + 2])
        canh.append((u, v, w)); adj[u].append(v)
    INF = float('inf')
    d = [INF] * (n + 1); d[1] = 0
    for _ in range(n - 1):
        doi = False
        for u, v, w in canh:
            if d[u] + w < d[v]:
                d[v] = d[u] + w; doi = True
        if not doi:
            break
    am = deque()                           # cac dinh van giam o vong thu n
    tham = bytearray(n + 1)
    for u, v, w in canh:
        if d[u] + w < d[v] and not tham[v]:
            tham[v] = 1; am.append(v)
    while am:                              # loang tu cac dinh "am vo cuc"
        u = am.popleft()
        for v in adj[u]:
            if not tham[v]:
                tham[v] = 1; am.append(v)
    if tham[n]:
        kq = 'VOCUC'
    elif d[n] == INF:
        kq = 'KHONG'
    else:
        kq = str(d[n])
    with open('THUONGPHAT.OUT', 'w') as f:
        f.write(kq + '\n')

main()
