# CATGO - cung cong thuc QHD nhung vong trong viet bang Python thuong.
# Dung, nhung n = 4000 thi 8*10^6 phep -> ~0.5 s may manh, co the > 1 s o may phong thi.
# Chac chan qua subtask 1, 2 (n <= 1000); subtask 3 tuy may.
def main():
    data = open('CATGO.INP', 'rb').read().split()
    n = int(data[0])
    p = [0] + list(map(int, data[1:1 + n]))
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        best = 0
        for j in range(1, i + 1):
            v = p[j] + f[i - j]
            if v > best:
                best = v
        f[i] = best
    with open('CATGO.OUT', 'w') as out:
        out.write(str(f[n]) + '\n')

main()
