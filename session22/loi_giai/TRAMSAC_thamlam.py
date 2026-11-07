# TRAMSAC - THAM LAM SAI (de doi chieu tim test phan vi du): "chay xa nhat co the roi moi sac".
# Cach nay toi thieu SO LAN sac, khong toi thieu TIEN. Test nho phan vi du: L = 10, P = 15,
#   tram (5, gia 1), (10, gia 100): tham lam sac o 10 (ton 100), toi uu sac o 5 (ton 1).
def main():
    data = open('TRAMSAC.INP', 'rb').read().split()
    n, L, P = int(data[0]), int(data[1]), int(data[2])
    x = [int(data[3 + 2 * i]) for i in range(n)] + [P]
    c = [int(data[4 + 2 * i]) for i in range(n)] + [0]
    cur, tien, i = 0, 0, 0
    while cur + L < P:
        j = i
        while j < n and x[j] <= cur + L:    # tram xa nhat trong tam
            j += 1
        if j == i:                           # khong co tram nao trong tam
            tien = -1
            break
        tien += c[j - 1]; cur = x[j - 1]; i = j
    with open('TRAMSAC.OUT', 'w') as f:
        f.write(str(tien) + '\n')

main()
