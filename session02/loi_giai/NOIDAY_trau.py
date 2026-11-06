# NOIDAY - ban cham: moi lan sap xep lai ca mang O(n^2 log n). Chi qua n <= 1000
def main():
    data = open('NOIDAY.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    ans = 0
    while len(a) > 1:
        a.sort()
        x = a.pop(0); y = a.pop(0)
        ans += x + y
        a.append(x + y)
    with open('NOIDAY.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
