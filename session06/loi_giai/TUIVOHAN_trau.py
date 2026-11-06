# TUIVOHAN - vet can: quay lui chon SO CAI cua tung loai. Chi qua subtask 1 (n <= 5, W <= 50)
def main():
    data = open('TUIVOHAN.INP', 'rb').read().split()
    n, W = int(data[0]), int(data[1])
    w = [int(data[2 + 2 * i]) for i in range(n)]
    v = [int(data[3 + 2 * i]) for i in range(n)]
    best = 0

    def thu(i, con, gt):                       # da chon xong loai 0..i-1, con 'con' suc chua
        nonlocal best
        if i == n:
            best = max(best, gt)
            return
        k = 0
        while k * w[i] <= con:
            thu(i + 1, con - k * w[i], gt + k * v[i])
            k += 1

    thu(0, W, 0)
    with open('TUIVOHAN.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
