# Sinh MOT test nho cho CAMERA (cay n <= 9 nut, chi phi 1..10). Cay ngau nhien: nut i noi voi mot nut < i.
import random, sys
random.seed(int(sys.argv[1]))
n = random.randint(1, 9)
print(n)
print(*[random.randint(1, 10) for _ in range(n)])
p = list(range(1, n + 1)); random.shuffle(p)          # tron nhan de goc 1 khong luon la "goc that"
for i in range(1, n):
    print(p[i], p[random.randrange(i)])
