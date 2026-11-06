# NOIDAY: noi n doan day, moi lan noi 2 doan chi phi = tong do dai. Tong chi phi nho nhat.
# Tham lam: luon noi 2 doan ngan nhat -> heapq. n <= 2*10^5, O(n log n)
import heapq

def main():
    data = open('NOIDAY.INP', 'rb').read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    heapq.heapify(h)                     # O(n), nhanh hon n lan heappush
    pop, rep = heapq.heappop, heapq.heapreplace
    ans = 0
    for _ in range(n - 1):
        x = pop(h)                       # doan ngan nhat
        y = h[0]                         # doan ngan thu hai (chua lay ra)
        ans += x + y
        rep(h, x + y)                    # lay y ra va dua x + y vao trong MOT thao tac
    with open('NOIDAY.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
