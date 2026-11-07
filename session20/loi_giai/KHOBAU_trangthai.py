# KHOBAU - cach "mot BFS tren do thi trang thai (o, tap kho bau da nhat)" - DUNG nhung CHAM:
# so trang thai R*C*2^k = 4*10^4 * 32768 ~ 1,3*10^9 -> khong the. Chi dung cho luoi nho, k nho (subtask 1).
# Bai hoc: chi cac o kho bau moi "quan trong"; nen do thi lai con k+1 dinh (BFS), roi moi QHD bitmask.
def main():
    data = open('KHOBAU.INP', 'rb').read().split()
    R, C = int(data[0]), int(data[1])
    W = C + 2
    o = bytearray(b'#' * ((R + 2) * W))
    so = {}                                           # o kho bau -> chi so bit
    s = 0
    for i in range(R):
        dong = data[2 + i]
        o[(i + 1) * W + 1:(i + 1) * W + 1 + C] = dong
        for j in range(C):
            p = (i + 1) * W + j + 1
            if dong[j] == 83:
                s = p
            elif dong[j] == 42:
                so[p] = len(so)
    k = len(so)
    full = (1 << k) - 1
    dist = {(s, 0): 0}
    hd = [(s, 0)]
    res = 0 if k == 0 else -1
    for p, m in hd:
        if m == full:
            res = dist[(p, m)]
            break
        d1 = dist[(p, m)] + 1
        for h in (1, -1, W, -W):
            q = p + h
            if o[q] == 35:
                continue
            nm = m | (1 << so[q]) if q in so else m
            if (q, nm) not in dist:
                dist[(q, nm)] = d1
                hd.append((q, nm))
    with open('KHOBAU.OUT', 'w') as f:
        f.write(str(res) + '\n')

main()
