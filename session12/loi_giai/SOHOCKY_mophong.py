# SOHOCKY - mo phong tung hoc ky: moi ky dem lai so mon tien quyet chua hoc cua moi mon (quet m canh),
# hoc tat ca mon dem duoc 0. O(so ky * (n + m)): dung, nhung chuoi 2*10^5 mon -> 2*10^5 ky -> qua gio.
def main():
    data = open('SOHOCKY.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    canh = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    xong = [False] * (n + 1)
    con, ky = n, 0
    while con:
        deg = [0] * (n + 1)
        for u, v in canh:
            if not xong[u]:
                deg[v] += 1
        moi = [u for u in range(1, n + 1) if not xong[u] and deg[u] == 0]
        if not moi:
            ky = -1                    # khong hoc them duoc mon nao: chu trinh
            break
        for u in moi:
            xong[u] = True
        con -= len(moi); ky += 1
    with open('SOHOCKY.OUT', 'w') as f:
        f.write(str(ky) + '\n')

main()
