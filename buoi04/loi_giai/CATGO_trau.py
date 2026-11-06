# CATGO - vet can: de quy thu do dai doan dau tien j, phan con lai giai tiep, KHONG nho
# So loi goi = 2^n (moi cach chia n thanh day so nguyen duong): chi qua subtask 1 (n <= 15).
# Them dict nho vao ham 'tot' la thanh QHD co nho O(n^2).
def main():
    data = open('CATGO.INP', 'rb').read().split()
    n = int(data[0])
    p = [0] + list(map(int, data[1:1 + n]))

    def tot(i):                         # tien lon nhat cho thanh dai i
        if i == 0:
            return 0
        return max(p[j] + tot(i - j) for j in range(1, i + 1))

    with open('CATGO.OUT', 'w') as out:
        out.write(str(tot(n)) + '\n')

main()
