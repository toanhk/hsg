# Sinh MOT test nho cho LEONUI (luoi <= 5 x 5, do cao 0..9).
import random, sys
random.seed(int(sys.argv[1]))
m, n = random.randint(1, 5), random.randint(1, 5)
print(m, n)
for _ in range(m):
    print(*[random.randint(0, 9) for _ in range(n)])
