# DOITIEN - vet can: quay lui chon SO TO cua tung loai (loai 0, 1, ..., m-1 theo thu tu)
# -> moi cach doi chi duoc dem 1 lan vi thu tu xet loai co dinh.
# Loai cuoi cung khong can thu: so tien con lai phai chia het cho menh gia cua no.
# So nut ~ so cach doi; chi qua subtask 1 (m <= 5, S <= 100).
def main():
    data = open('DOITIEN.INP', 'rb').read().split()
    m, S = int(data[0]), int(data[1])
    c = list(map(int, data[2:2 + m]))
    dem = 0

    def thu(i, con):                    # da chon xong loai 0..i-1, con lai 'con' dong
        nonlocal dem
        if i == m - 1:
            if con % c[i] == 0:
                dem += 1
            return
        so_to = 0
        while so_to * c[i] <= con:
            thu(i + 1, con - so_to * c[i])
            so_to += 1

    thu(0, S)
    with open('DOITIEN.OUT', 'w') as out:
        out.write(str(dem % (10**9 + 7)) + '\n')

main()
