# CAMERA - vet can (n <= 15): thu moi tap nut dat camera, kiem tra moi nut duoc giam sat.
def main():
    data = open('CAMERA.INP', 'rb').read().split()
    n = int(data[0])
    c = list(map(int, data[1:1 + n]))
    ke = [1 << i for i in range(n)]               # ke[v] = tap nut v giam sat (gom chinh v)
    pos = 1 + n
    for _ in range(n - 1):
        u, v = int(data[pos]) - 1, int(data[pos + 1]) - 1; pos += 2
        ke[u] |= 1 << v; ke[v] |= 1 << u
    full = (1 << n) - 1
    best = None
    for mask in range(1, 1 << n):
        gs = 0; tien = 0
        for v in range(n):
            if mask >> v & 1:
                gs |= ke[v]; tien += c[v]
        if gs == full and (best is None or tien < best):
            best = tien
    with open('CAMERA.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
