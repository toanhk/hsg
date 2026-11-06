# COPHIEU: biet gia co phieu n ngay p[1..n]. Mua 1 lan o ngay i, ban 1 lan o ngay j > i.
# Lai lon nhat? Neu khong co lai thi khong giao dich (in 0). n <= 10^6, p[i] <= 10^9
#   Trang thai : f[j] = lai lon nhat neu BAN vao ngay j = p[j] - min(p[1..j-1])
#   Truy hoi   : giu thap = min(p[1..j-1]) cap nhat dan, khong can mang
#   Khoi tao   : thap = p[1], tot = 0
#   Thu tu     : j tang dan (tinh f[j] TRUOC roi moi cap nhat thap bang p[j])
#   Dap an     : max(0, max f[j])
def main():
    data = open('COPHIEU.INP', 'rb').read().split()
    n = int(data[0])
    p = map(int, data[1:1 + n])
    thap = next(p)
    tot = 0
    for x in p:
        if x - thap > tot:
            tot = x - thap
        elif x < thap:                  # x < thap thi x - thap < 0 <= tot, khong the vao nhanh tren
            thap = x
    with open('COPHIEU.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
