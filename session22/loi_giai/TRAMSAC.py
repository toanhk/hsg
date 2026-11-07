# TRAMSAC (de thi thu so 2, bai 1, 6 diem) - QHD mot chieu + heapq lay min trong cua so
# Xe dien di tu vi tri 0 den P, pin day chay duoc toi da L km. Tram i o x[i] (0 < x1 < ... < xn < P),
# sac day o tram i ton c[i]. Chi phi nho nhat de den P (-1 neu khong the). n <= 2*10^5.
# QHD:
#   Trang thai : f[i] = chi phi nho nhat de den tram i VA sac o do (f[0] = 0 tai vi tri 0, xuat phat day pin).
#   Cong thuc  : f[i] = c[i] + min{ f[j] : j < i, x[i] - x[j] <= L }.
#   Khoi tao   : f[0] = 0, x[0] = 0.
#   Thu tu     : i tang dan (x tang dan).
#   Dap an     : min{ f[j] : P - x[j] <= L }, khong co thi -1.
# Lay min trong cua so [x[i] - L, x[i]]: heap (f[j], x[j]); dinh heap co x[j] < x[i] - L thi bo luon
# (x tang dan nen tram da ra khoi tam se khong bao gio quay lai) -> O(n log n). Do ~0,3 s voi n = 2*10^5.
import heapq

def main():
    data = open('TRAMSAC.INP', 'rb').read().split()
    n, L, P = int(data[0]), int(data[1]), int(data[2])
    heap = [(0, 0)]                         # (f[j], x[j]); bat dau o vi tri 0, chi phi 0
    pos = 3
    for _ in range(n):
        x, c = int(data[pos]), int(data[pos + 1]); pos += 2
        while heap and heap[0][1] < x - L:  # tram qua xa phia sau -> bo vinh vien
            heapq.heappop(heap)
        if heap:                            # den duoc tram nay
            heapq.heappush(heap, (heap[0][0] + c, x))
    while heap and heap[0][1] < P - L:
        heapq.heappop(heap)
    ans = heap[0][0] if heap else -1
    with open('TRAMSAC.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
