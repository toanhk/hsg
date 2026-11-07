# Sinh MOT test nho cho XEPLICH (n <= 8 viec trong 12 ngay, tien 1..20) de doi chieu voi trau.
import random, sys
random.seed(int(sys.argv[1]))
n = random.randint(1, 8)
print(n)
for _ in range(n):
    s = random.randint(1, 12); e = random.randint(s, min(12, s + 4))
    print(s, e, random.randint(1, 20))
