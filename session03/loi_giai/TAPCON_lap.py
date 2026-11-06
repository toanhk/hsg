# TAPCON - cach 2: sinh tong cua moi tap con bang vong lap (khong de quy)
# tongs ban dau [0]; them phan tu x: moi tong cu t sinh them t + x  ->  sau n buoc co 2^n tong
# Cat nhanh: bo cac tong > S. List comprehension chay nhanh hon goi ham de quy nhieu lan
def main():
    data = open('TAPCON.INP', 'rb').read().split()
    n, S = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    tongs = [0]
    for x in a:
        tongs += [t + x for t in tongs if t + x <= S]
    with open('TAPCON.OUT', 'w') as f:
        f.write(str(tongs.count(S)) + '\n')

main()
