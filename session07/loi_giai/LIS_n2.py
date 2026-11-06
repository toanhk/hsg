# LIS - QHD O(n^2): qua subtask 1, 2 (n <= 3000 ~ 0.3 s); n = 5*10^5 thi 1.25*10^11 phep -> qua gio
#   Trang thai : f[i] = do dai day con tang dai nhat KET THUC TAI a[i]
#   Truy hoi   : f[i] = 1 + max( f[j] ) voi j < i va a[j] < a[i]  (khong co j nao -> f[i] = 1)
#   Khoi tao   : f[i] = 1 (chi gom rieng a[i])
#   Thu tu     : i tang dan
#   Dap an     : max(f)  -- KHONG phai f[n-1]: day dai nhat co the ket thuc o bat ky dau
# Truy vet: luu tr[i] = j tot nhat, tu i co f lon nhat lan nguoc tr[] (in nguoc lai).
def main():
    data = open('LIS.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    f = [1] * n
    for i in range(n):
        ai = a[i]
        tot = 0
        for j in range(i):
            if a[j] < ai and f[j] > tot:
                tot = f[j]
        f[i] = tot + 1
    with open('LIS.OUT', 'w') as out:
        out.write(str(max(f)) + '\n')

main()
