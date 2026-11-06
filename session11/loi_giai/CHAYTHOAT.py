# CHAYTHOAT: toa nha m x n gom '.' (trong), '#' (tuong), 'J' (Binh dung o phut 0), 'F' (o dang chay
# o phut 0, co the nhieu o hoac khong co). Moi phut, dong thoi: Binh di sang 1 o ke canh khong phai
# tuong (hoac buoc ra ngoai neu dang dung o mep), va lua lan sang moi o khong phai tuong ke canh o dang
# chay. Binh khong duoc vao o da chay hoac bat lua dung luc Binh toi. Thoat nhanh nhat sau bao nhieu
# phut? Khong thoat duoc in -1. m, n <= 1000
# Hai lan BFS:
#  1) BFS NHIEU NGUON tu moi o F: lua[p] = phut o p bat lua (VC neu khong bao gio).
#  2) BFS tu J theo tang: o tang d (phut d), di sang v o phut d+1 chi khi lua[v] > d + 1.
#     Vien la ky tu 'O' (ngoai nha): BFS cua Binh cham toi 'O' lan dau o tang d+1 -> dap an d+1.
# Lua khong lan ra 'O' vi lua chi lan vao o '.' hoac 'J'.
def main():
    data = open('CHAYTHOAT.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    W = n + 2
    vien = b'O' * W
    s = vien + b''.join(b'O' + r + b'O' for r in data[2:2 + m]) + vien
    VC = 10**9
    TUONG, NGOAI = 35, 79                    # '#', 'O'
    # lua[p]: -1 = chua biet (o di duoc), -2 = tuong, VC = ngoai nha (lua khong bao gio toi)
    lua = [-2 if c == TUONG else VC if c == NGOAI else -1 for c in s]
    tang = []
    p = s.find(b'F')
    while p >= 0:
        lua[p] = 0
        tang.append(p)
        p = s.find(b'F', p + 1)
    d = 0
    while tang:
        d += 1
        ke = []
        for p in tang:
            for v in (p - W, p + W, p - 1, p + 1):
                if lua[v] == -1:
                    lua[v] = d
                    ke.append(v)
        tang = ke
    lua = [VC if x == -1 else x for x in lua]   # o lua khong toi -> VC; tuong van la -2
    # BFS cua Binh. Tuong co lua = -2 nen dieu kien lua[v] > d + 1 tu loai tuong.
    tham = bytearray(len(s))
    J = s.find(b'J')
    tham[J] = 1
    tang = [J]
    d = 0
    kq = -1
    while tang and kq < 0:
        ke = []
        for p in tang:
            for v in (p - W, p + W, p - 1, p + 1):
                if not tham[v] and lua[v] > d + 1:
                    if s[v] == NGOAI:
                        kq = d + 1
                        break
                    tham[v] = 1
                    ke.append(v)
            if kq >= 0:
                break
        d += 1
        tang = ke
    with open('CHAYTHOAT.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
