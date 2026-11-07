# CATDX - CHAM: QHD mot chieu dung, nhung kiem tra doan doi xung bang cat lat t == t[::-1] moi lan
# -> O(n^3) (moi cap (l, i) ton O(do dai)). Cat lat va so sanh chay bang C nen chi cham hon ~3 lan:
# do tren may cloud n = 2000 mat 0,57-0,67 s (ban chinh 0,11-0,27 s) -> qua sat 1 s, may phong thi de qua gio.
# Bai hoc: bang dx[l][r] (QHD tren doan) bien moi lan hoi "doan nay doi xung?" thanh O(1).
def main():
    data = open('CATDX.INP', 'rb').read().split()
    S = data[0]
    n = len(S)
    g = [0] * (n + 1)
    for i in range(1, n + 1):
        best = i
        for l in range(i):
            t = S[l:i]
            if t == t[::-1] and g[l] + 1 < best:
                best = g[l] + 1
        g[i] = best
    with open('CATDX.OUT', 'w') as out:
        out.write(str(g[n]) + '\n')

main()
