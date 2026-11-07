# DUTIEC - vet can (n <= 20): thu moi tap con (bitmask), bo tap co ca i va p[i]. O(2^n * n).
def main():
    data = open('DUTIEC.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))                       # a[i] cua nguoi i+1
    p = [-1] + [int(x) - 1 for x in data[n + 1:2 * n]]      # danh so tu 0
    best = 0
    for mask in range(1 << n):
        ok = True; t = 0
        for i in range(n):
            if mask >> i & 1:
                if i > 0 and mask >> p[i] & 1:
                    ok = False; break
                t += a[i]
        if ok and t > best:
            best = t
    with open('DUTIEC.OUT', 'w') as f:
        f.write(str(best) + '\n')

main()
