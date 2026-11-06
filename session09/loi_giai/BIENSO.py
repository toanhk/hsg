# BIENSO: Tren man hinh co so A. Moi lan bam nut, so x doi thanh x + 1, x - 1 hoac 2x.
# Moi so xuat hien tren man hinh phai nam trong doan [0, 10^6]. Hoi it nhat bao nhieu lan bam
# de duoc so B. 0 <= A, B <= 10^6.
# Mo hinh: DO THI AN - moi so 0..10^6 la mot dinh, moi phep bam la mot canh co huong.
# Khong can dung danh sach ke: canh cua x tinh ngay khi can (x+1, x-1, 2x). BFS tu A.
#   dist[x] = so lan bam it nhat tu A den x; -1 = chua tham
#   Chan bien CA HAI PHIA: y >= 0 va y <= L. Thieu y >= 0 thi dist[-1] la dist[L] (Python
#   khong bao loi chi so am) -> sai lang le (xem BIENSO_sai.py).
# Toi da 10^6 + 1 dinh x 3 canh: ~0,25 giay khi viet 3 lenh if (for y in (...) cham hon ~1,6 lan).
from collections import deque

L = 10**6

def main():
    A, B = map(int, open('BIENSO.INP', 'rb').read().split()[:2])
    dist = [-1] * (L + 1)
    dist[A] = 0
    q = deque([A])
    push = q.append; pop = q.popleft          # gan san ham cho nhanh
    while dist[B] < 0:                         # B duoc tham la dung: dist[B] da toi uu
        x = pop()
        d = dist[x] + 1
        y = x + 1
        if y <= L and dist[y] < 0:
            dist[y] = d; push(y)
        y = x - 1
        if y >= 0 and dist[y] < 0:
            dist[y] = d; push(y)
        y = 2 * x
        if y <= L and dist[y] < 0:
            dist[y] = d; push(y)
    with open('BIENSO.OUT', 'w') as f:
        f.write(str(dist[B]) + '\n')

main()
