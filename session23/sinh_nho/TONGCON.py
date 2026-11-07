# Sinh MOT test nho cho TONGCON (n <= 10, a[i] trong 0..5 - co nhieu so 0 de bat loi bien).
import random, sys
random.seed(int(sys.argv[1]))
n = random.randint(1, 10)
a = [random.randint(0, 5) for _ in range(n)]
L = random.randint(0, 15); R = random.randint(L, 20)
print(n, L, R); print(*a)
