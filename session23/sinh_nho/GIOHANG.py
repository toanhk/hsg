# Sinh MOT test nho cho GIOHANG (n <= 8 mon, it nhom de hay trung nhom).
import random, sys
random.seed(int(sys.argv[1]))
n = random.randint(1, 8); B = random.randint(1, 20)
print(n, B)
for _ in range(n):
    print(random.randint(1, 3), random.randint(1, B), random.randint(1, 20))
