# MECUNG: me cung m x n gom '.' (trong), '#' (tuong), 'S' (xuat phat), 'E' (loi ra). Moi buoc di
# sang o ke CANH khong phai tuong. So buoc it nhat tu S den E? Khong toi duoc in -1. m, n <= 1000
# Mo hinh: dinh = o, canh = 2 o ke canh deu khong phai tuong, moi canh dai 1 -> BFS tu S.
# Meo toc do: vien tuong + ma hoa o p = (i+1)*W + (j+1); dist = -1 (chua tham) / -2 (tuong, vien)
# nen kiem tra "di vao duoc va chua tham" chi bang 1 phep so sanh dist[v] == -1.
# BFS THEO TANG: tang = cac o cach S dung d buoc; gap E thi dung ngay.
# O(m*n), 10^6 o ~0.2 s (BFS deque + tuple + kiem tra bien mat ~0.7 s, xem do_loang.py).
def main():
    data = open('MECUNG.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    vien = b'#' * W
    s = vien + b''.join(b'#' + r + b'#' for r in data[2:2 + m]) + vien
    S, E = s.find(b'S'), s.find(b'E')
    dist = [-2 if c == 35 else -1 for c in s]    # 35 = '#'
    dist[S] = 0
    tang = [S]
    d = 0
    kq = -1
    if S == E:
        kq = 0
    while tang and kq < 0:
        d += 1
        ke = []
        for p in tang:
            for v in (p - W, p + W, p - 1, p + 1):
                if dist[v] == -1:
                    dist[v] = d
                    ke.append(v)
        if dist[E] >= 0:
            kq = d
        tang = ke
    with open('MECUNG.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
