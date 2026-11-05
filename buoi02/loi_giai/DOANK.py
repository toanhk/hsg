# DOANK: dem so doan con lien tiep co tong dung bang K (a[i] co the am). n <= 10^6
# Doan (l, r] co tong K  <=>  s[r] - s[l] = K  <=>  s[l] = s[r] - K
# -> giong CAPK tren mang cong don s[0..n]. O(n)
from itertools import accumulate

def main():
    data = open('DOANK.INP', 'rb').read().split()
    n, k = int(data[0]), int(data[1])
    dem = {0: 1}                 # s[0] = 0 da xuat hien 1 lan
    get = dem.get
    ans = 0
    for s in accumulate(map(int, data[2:2 + n])):
        ans += get(s - k, 0)
        dem[s] = get(s, 0) + 1
    with open('DOANK.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
