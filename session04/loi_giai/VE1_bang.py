# VE1 - QHD bang (bottom-up) theo dung 3 thao tac, KHONG can nhan xet "tru n % 2":
#   f[i] = 1 + min( f[i-1], f[i/2] neu i chan, f[i/3] neu i chia het 3 ),  f[1] = 0
# Lap mot lan den max n roi tra loi tung truy van. Qua subtask 1, 2 (n <= 10^6, ~0.4 s);
# n = 10^18 thi khong co du bo nho lan thoi gian -> phai dung ban co nho (VE1.py).
def main():
    data = open('VE1.INP', 'rb').read().split()
    t = int(data[0])
    q = [int(x) for x in data[1:1 + t]]
    m = max(q)
    f = [0] * (m + 1)
    for i in range(2, m + 1):
        b = f[i - 1]
        if i % 2 == 0 and f[i // 2] < b:
            b = f[i // 2]
        if i % 3 == 0 and f[i // 3] < b:
            b = f[i // 3]
        f[i] = b + 1
    with open('VE1.OUT', 'w') as out:
        out.write('\n'.join(str(f[n]) for n in q) + '\n')

main()
