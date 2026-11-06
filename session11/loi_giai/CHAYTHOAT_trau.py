# CHAYTHOAT - vet can: MO PHONG tung phut. Giu tap o dang chay va tap cac o Binh CO THE dang dung.
# Phut t -> t+1: tinh tap lua moi truoc, roi Binh tu moi o co the dung buoc sang o ke khong phai tuong
# va khong nam trong tap lua moi; buoc ra ngoai bang -> thoat o phut t+1. Chi subtask 1 (m, n <= 20).
def main():
    data = open('CHAYTHOAT.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = [r.decode() for r in data[2:2 + m]]
    lua = {(i, j) for i in range(m) for j in range(n) if g[i][j] == 'F'}
    binh = {(i, j) for i in range(m) for j in range(n) if g[i][j] == 'J'}
    da_den = set(binh)
    t = 0
    kq = -1
    while binh and kq < 0:
        lua_moi = set(lua)
        for i, j in lua:
            for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= u < m and 0 <= v < n and g[u][v] != '#':
                    lua_moi.add((u, v))
        moi = set()
        for i, j in binh:
            for u, v in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= u < m and 0 <= v < n):
                    kq = t + 1
                elif g[u][v] != '#' and (u, v) not in lua_moi and (u, v) not in da_den:
                    moi.add((u, v))
        da_den |= moi
        lua, binh = lua_moi, moi
        t += 1
    with open('CHAYTHOAT.OUT', 'w') as f:
        f.write(str(kq) + '\n')

main()
