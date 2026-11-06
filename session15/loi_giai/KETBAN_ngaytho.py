# KETBAN - DSU "ngay tho": KHONG nen duong, KHONG hop theo kich thuoc (luon cha[a] = b).
# Dung, nhung cay co the thanh mot CHUOI dai: thao tac "1 1 2", "1 1 3", "1 1 4", ... moi lan noi
# goc cu vao dinh moi -> find(1) phai di qua ca chuoi, O(n) moi lan -> O(n*q) ~ 4*10^10.
# Dung de chua bai: chi qua subtask 1-2.

def main():
    data = open('KETBAN.INP', 'rb').read().split()
    n, q = int(data[0]), int(data[1])
    cha = list(range(n + 1))

    def find(x):
        while cha[x] != x:
            x = cha[x]
        return x

    out = []
    for i in range(2, 2 + 3 * q, 3):
        a = find(int(data[i + 1])); b = find(int(data[i + 2]))
        if data[i] == b'1':
            if a != b:
                cha[a] = b
        else:
            out.append('CO' if a == b else 'KHONG')
    with open('KETBAN.OUT', 'w') as f:
        f.write('\n'.join(out) + '\n')

main()
