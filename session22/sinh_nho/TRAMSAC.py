# Sinh MOT test nho cho TRAMSAC (n <= 8) de doi chieu voi trau. Chay: python sinh_nho/TRAMSAC.py 17
import random, sys
random.seed(int(sys.argv[1]))
n = random.randint(1, 8)
P = random.randint(n + 1, 30)
x = sorted(random.sample(range(1, P), n))
L = random.randint(1, 12)
print(n, L, P)
for v in x:
    print(v, random.randint(1, 20))
