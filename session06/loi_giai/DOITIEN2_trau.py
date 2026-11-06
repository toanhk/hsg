# DOITIEN2 - vet can: quay lui chon so to tung loai. Chi qua subtask 1 (m <= 3, S <= 100)
def main():
    data = open('DOITIEN2.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + m]))
    best = -1

    def thu(i, con, dem):
        nonlocal best
        if i == m:
            if con == 0 and (best < 0 or dem < best):
                best = dem
            return
        k = 0
        while k * c[i] <= con:
            thu(i + 1, con - k * c[i], dem + k)
            k += 1

    thu(0, S, 0)
    with open('DOITIEN2.OUT', 'w') as out:
        out.write(str(best) + '\n')

main()
