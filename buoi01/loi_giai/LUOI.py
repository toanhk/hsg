# LUOI: bang m x n ky tu '.'/'#'. In tong so o '#', hang va cot co nhieu '#' nhat
def main():
    data = open('LUOI.INP', 'rb').read().split()
    m, n = int(data[0]), int(data[1])
    g = data[2:2 + m]                       # moi hang la mot bytes
    hang = [row.count(b'#') for row in g]
    THANG = ord('#')                        # 35: g[i][j] la so nguyen
    cot = [col.count(THANG) for col in zip(*g)]   # zip(*g) lay tung cot
    h = hang.index(max(hang)) + 1           # index tra ve vi tri dau tien = chi so nho nhat
    c = cot.index(max(cot)) + 1
    with open('LUOI.OUT', 'w') as f:
        f.write(f'{sum(hang)}\n{h}\n{c}\n')

main()
