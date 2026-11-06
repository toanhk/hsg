# DOANMAX: doan con lien tiep (khac rong) co tong lon nhat. n <= 10^6, |a[i]| <= 10^9
# Thuat toan Kadane.
#   Trang thai : f[i] = tong lon nhat cua doan KET THUC TAI i (bat buoc chua a[i])
#   Truy hoi   : f[i] = a[i] + max(f[i-1], 0)  (noi tiep doan truoc neu no duong, khong thi bat dau lai)
#   Khoi tao   : f[1] = a[1]
#   Thu tu     : i tang dan
#   Dap an     : max(f[1..n])  -- KHONG phai f[n]: doan tot nhat co the ket thuc o bat ky dau
# Loi hay gap: khoi tao tot = 0 -> sai khi moi a[i] am (doan phai khac rong).
def main():
    data = open('DOANMAX.INP', 'rb').read().split()
    n = int(data[0])
    a = map(int, data[1:1 + n])
    cur = tot = next(a)                 # f[1] = a[1]
    for x in a:
        if cur > 0:
            cur += x
        else:
            cur = x
        if cur > tot:
            tot = cur
    with open('DOANMAX.OUT', 'w') as out:
        out.write(str(tot) + '\n')

main()
