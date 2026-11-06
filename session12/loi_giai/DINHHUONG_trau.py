# DINHHUONG - vet can (k <= 12 canh vo huong): thu moi 2^k cach dinh huong, kiem tra khong chu trinh
# bang cach lap xoa dinh co bac vao 0 (Kahn don gian O(n^2)).
def khong_vong(n, cung):
    deg = [0] * (n + 1)
    for u, v in cung:
        deg[v] += 1
    con = set(range(1, n + 1))
    while True:
        x = next((u for u in con if deg[u] == 0), None)
        if x is None:
            return not con
        con.remove(x)
        for u, v in cung:
            if u == x:
                deg[v] -= 1

def main():
    data = open('DINHHUONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    co, vo = [], []
    for i in range(m):
        t, u, v = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
        (co if t == 1 else vo).append((u, v))
    k = len(vo)
    kq = '-1'
    for mask in range(1 << k):
        cung = co + [(v, u) if mask >> j & 1 else (u, v) for j, (u, v) in enumerate(vo)]
        if khong_vong(n, cung):
            kq = ''.join('1' if mask >> j & 1 else '0' for j in range(k))
            break
    with open('DINHHUONG.OUT', 'w') as f:
        f.write(kq + '\n')

main()
