# CAPK: dem cap (i < j) co a[i] + a[j] = K. n <= 5*10^5. Dung dict: O(n)
def main():
    data = open('CAPK.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    dem = {}                    # dem[x] = so lan x da xuat hien BEN TRAI vi tri hien tai
    ans = 0
    get = dem.get               # gan ham vao bien cuc bo cho nhanh
    for x in a:
        ans += get(k - x, 0)    # ghep x voi moi phan tu ben trai bang k - x
        dem[x] = get(x, 0) + 1  # roi moi them x (de khong ghep x voi chinh no)
    with open('CAPK.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
