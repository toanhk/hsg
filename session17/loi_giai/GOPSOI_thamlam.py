# GOPSOI - THAM LAM (SAI): moi buoc gop cap dong ke nhau co TONG NHO NHAT.
# Phan vi du: a = 5 2 4 4 -> tham lam gop (2,4)=6, (6,4)=10, (5,10)=15: 31; toi uu (5,2), (4,4), (7,8): 30.
# Dung de chua bai: "gop hai dong nho nhat" chi dung khi duoc gop HAI DONG BAT KY (bai NOIDAY buoi 2, heapq);
# rang buoc KE NHAU lam tham lam hong -> phai QHD tren doan.
def main():
    data = open('GOPSOI.INP', 'rb').read().split()
    n = int(data[0])
    d = list(map(int, data[1:1 + n]))
    tong = 0
    while len(d) > 1:
        i = min(range(len(d) - 1), key=lambda j: d[j] + d[j + 1])
        s = d[i] + d[i + 1]
        tong += s
        d[i:i + 2] = [s]
    with open('GOPSOI.OUT', 'w') as out:
        out.write(str(tong) + '\n')

main()
