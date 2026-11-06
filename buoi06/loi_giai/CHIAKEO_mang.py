# CHIAKEO - ban mang bytearray (QHD 0/1 thuong). O(n * tong/2): qua subtask 1, 2 (tong <= 10^4)
def main():
    data = open('CHIAKEO.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    tong = sum(a)
    nua = tong // 2
    duoc = bytearray(nua + 1)
    duoc[0] = 1
    for x in a:
        for s in range(nua, x - 1, -1):        # s giam dan: moi goi dung toi da 1 lan
            if duoc[s - x]:
                duoc[s] = 1
    t = nua
    while not duoc[t]:
        t -= 1
    with open('CHIAKEO.OUT', 'w') as out:
        out.write(str(tong - 2 * t) + '\n')

main()
