# Sinh MOT test nho cho PHATUONG: 1..3 bo test, luoi <= 5 x 5 (nhieu bo test de bat loi quen reset).
import random, sys
random.seed(int(sys.argv[1]))
t = random.randint(1, 3)
print(t)
for _ in range(t):
    r, c = random.randint(1, 5), random.randint(1, 5)
    while r * c < 2:
        r, c = random.randint(1, 5), random.randint(1, 5)
    g = [['#' if random.random() < 0.45 else '.' for _ in range(c)] for _ in range(r)]
    o = random.sample(range(r * c), 2)
    g[o[0] // c][o[0] % c] = 'S'; g[o[1] // c][o[1] % c] = 'T'
    print(r, c)
    for row in g:
        print(''.join(row))
