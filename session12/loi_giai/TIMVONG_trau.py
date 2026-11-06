# TIMVONG - vet can (n <= 8): thu moi day dinh phan biet v1..vk (k = 1..n), kiem tra la chu trinh.
from itertools import permutations

def main():
    data = open('TIMVONG.INP', 'rb').read().split()
    n, m = int(data[0]), int(data[1])
    co = set()
    for i in range(m):
        co.add((int(data[2 + 2 * i]), int(data[3 + 2 * i])))
    kq = '-1'
    for k in range(1, n + 1):
        for p in permutations(range(1, n + 1), k):
            if all((p[i], p[(i + 1) % k]) in co for i in range(k)):
                kq = f'{k}\n' + ' '.join(map(str, p))
                break
        if kq != '-1':
            break
    with open('TIMVONG.OUT', 'w') as f:
        f.write(kq + '\n')

main()
