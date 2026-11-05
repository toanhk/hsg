# Lộ trình bồi dưỡng HSG Tin cấp tỉnh — Đồ thị & QHĐ (Python)

## Tổng quan

Lộ trình gồm 24 buổi (mỗi buổi khoảng 3 giờ), chia 6 giai đoạn, đưa học sinh từ Python cơ bản đến giải được bài Đồ thị và QHĐ mức đề HSG cấp tỉnh bằng Python.

**Đối tượng:** học sinh THPT đã biết cú pháp Python (biến, vòng lặp, hàm, list, dict).

**Hình thức thi cấp tỉnh thường gặp** (cần đối chiếu công văn của Sở năm nay): 3–4 bài trong 150–180 phút, đọc/ghi file `.INP`/`.OUT`, chấm tự động bằng bộ test (thường là Themis), đề chia subtask theo giới hạn n. Giới hạn thời gian ~1 giây/test là bất lợi lớn với Python, nên lộ trình dành riêng phần tối ưu tốc độ.

**Mục tiêu đầu ra:** lấy trọn subtask nhỏ của mọi bài, giải trọn ít nhất 2 bài Đồ thị/QHĐ mức trung bình, và biết nhận ra dạng bài trong 10 phút đầu.

| Giai đoạn | Buổi | Nội dung chính |
| --- | --- | --- |
| 1. Python thi đấu & nền tảng | 1–3 | I/O nhanh, độ phức tạp, đệ quy, quay lui |
| 2. QHĐ cơ bản | 4–8 | QHĐ 1 chiều, cái túi, LIS, LCS, QHĐ trên lưới |
| 3. Đồ thị cơ bản | 9–12 | Biểu diễn, BFS, DFS, liên thông, loang lưới, tô-pô |
| 4. Đường đi & cây khung | 13–16 | Dijkstra, BFS 0-1, Floyd, DSU, Kruskal |
| 5. QHĐ nâng cao & kết hợp | 17–20 | QHĐ đoạn, bitmask, trên cây, trên DAG, đếm có modulo |
| 6. Tổng hợp & thi thử | 21–24 | Đề các năm, thi thử tính giờ, chữa bài |

Quy tắc chung mỗi buổi: 30 phút lý thuyết + ví dụ, 90 phút làm bài, 45 phút chữa bài, 15 phút giao bài về nhà (3–5 bài, từ dễ đến khó).

## Giai đoạn 1 — Python cho thi đấu và nền tảng (buổi 1–3)

Học sinh phải viết được chương trình Python đọc file nhanh và ước lượng được thuật toán có qua giới hạn thời gian hay không trước khi học Đồ thị và QHĐ.

| Buổi | Chủ đề | Nội dung | Bài luyện gợi ý |
| --- | --- | --- | --- |
| 1 | Khung bài thi & I/O nhanh | Đọc/ghi `.INP`/`.OUT`, `sys.stdin.readline`, đọc toàn bộ bằng `sys.stdin.buffer.read().split()`, ghi một lần bằng `'\n'.join` | Bài tính tổng/đếm với n = 10^6 để so thời gian `input()` và đọc nhanh |
| 2 | Độ phức tạp & cấu trúc dữ liệu sẵn có | Big-O; quy tắc ~10^7 phép tính/giây với Python; `list`, `dict`, `set`, `deque`, `heapq`, `bisect`; mảng cộng dồn | Tổng đoạn con, đếm cặp có tổng bằng K, tìm kiếm nhị phân |
| 3 | Đệ quy & quay lui | Liệt kê xâu nhị phân, hoán vị, tổ hợp; giới hạn đệ quy của Python và `sys.setrecursionlimit`; nhận ra quay lui là "QHĐ chưa nhớ" | Liệt kê tập con có tổng bằng S, bài toán 8 quân hậu |

Kiểm tra cuối giai đoạn: mỗi học sinh nộp một file khung `template.py` đúng chuẩn đọc/ghi file của kỳ thi.

## Giai đoạn 2 — Quy hoạch động cơ bản (buổi 4–8)

Mục tiêu là học sinh tự xây được 5 thành phần của một lời giải QHĐ: trạng thái, công thức truy hồi, khởi tạo, thứ tự tính, vị trí đáp án. Dạy QHĐ trước đồ thị vì nó chỉ cần mảng và vòng lặp, hợp với học sinh vừa xong giai đoạn 1.

| Buổi | Chủ đề | Nội dung | Bài luyện gợi ý |
| --- | --- | --- | --- |
| 4 | Từ đệ quy đến QHĐ | Fibonacci: đệ quy → nhớ (memo) → bảng (bottom-up); vì sao Python nên ưu tiên bottom-up | Leo cầu thang 1–2–3 bước, đếm cách đổi tiền |
| 5 | QHĐ một chiều | Tổng lớn nhất không chọn 2 phần tử kề nhau, đoạn con có tổng lớn nhất (Kadane), đếm số cách theo modulo 10^9+7 | Ếch nhảy, mua bán cổ phiếu 1 lần |
| 6 | Cái túi | Cái túi 0/1, cái túi không giới hạn; tối ưu bộ nhớ còn 1 mảng (duyệt ngược); truy vết | Chia kẹo cân bằng nhất, đổi tiền ít tờ nhất |
| 7 | Dãy con | LIS O(n²) rồi O(n log n) bằng `bisect`; LCS hai xâu; khoảng cách sửa xâu | Xếp tháp hộp, xâu đối xứng dài nhất sau khi xóa |
| 8 | QHĐ trên lưới | Đường đi tổng lớn nhất trên bảng (chỉ đi phải/xuống), đếm đường đi có ô cấm, hình vuông lớn nhất toàn số 1 | Robot nhặt vàng, hình vuông con lớn nhất |

Kiểm tra cuối giai đoạn: 1 đề 3 bài trong 120 phút, mỗi bài học sinh phải viết ra giấy 5 thành phần QHĐ trước khi code.

## Giai đoạn 3 — Đồ thị cơ bản (buổi 9–12)

Học sinh cần biến đề bài thành đồ thị (đỉnh là gì, cạnh là gì) và cài đặt BFS/DFS không đệ quy để tránh lỗi tràn ngăn xếp của Python.

| Buổi | Chủ đề | Nội dung | Bài luyện gợi ý |
| --- | --- | --- | --- |
| 9 | Biểu diễn & BFS | Danh sách kề bằng `list` của `list`; BFS với `deque`; đường đi ít cạnh nhất và truy vết | Đường đi ngắn nhất giữa 2 thành phố, số bước tối thiểu biến số A thành B |
| 10 | DFS & liên thông | DFS bằng ngăn xếp tường minh; đếm thành phần liên thông; kiểm tra chu trình; đồ thị hai phía | Đếm nhóm bạn, chia hai đội không xung đột |
| 11 | Loang trên lưới | BFS/DFS trên bảng m×n, mảng `dx, dy`; BFS nhiều nguồn; mã hóa ô (i, j) thành `i*n + j` cho nhanh | Đếm hòn đảo, lửa lan, mê cung, quân mã |
| 12 | Sắp xếp tô-pô | Thuật toán Kahn (bậc vào + hàng đợi); phát hiện chu trình trên đồ thị có hướng; dẫn sang QHĐ trên DAG | Xếp lịch môn học tiên quyết, thứ tự công việc |

Kiểm tra cuối giai đoạn: 1 đề 3 bài trong 120 phút, trong đó có 1 bài lưới 1000×1000 để kiểm tra tốc độ Python.

## Giai đoạn 4 — Đường đi ngắn nhất, cây khung, DSU (buổi 13–16)

Đây là nhóm thuật toán xuất hiện nhiều nhất trong đề đồ thị cấp tỉnh; trọng tâm là Dijkstra với `heapq` và DSU.

| Buổi | Chủ đề | Nội dung | Bài luyện gợi ý |
| --- | --- | --- | --- |
| 13 | Dijkstra | Dijkstra với `heapq`, bỏ qua đỉnh lỗi thời (`if d > dist[u]: continue`); truy vết đường đi | Đường đi ngắn nhất từ 1 đến n, đi qua đỉnh trung gian bắt buộc |
| 14 | Biến thể đường đi | BFS 0-1, đồ thị nhiều trạng thái (đỉnh, số vé giảm giá còn lại), Floyd với n ≤ 200, Bellman-Ford và chu trình âm (giới thiệu) | Đi xe có 1 lần miễn phí, khoảng cách mọi cặp thành phố |
| 15 | DSU | Disjoint Set Union với nén đường + hợp theo kích thước, viết `find` không đệ quy; trả lời truy vấn liên thông | Nối đường dần theo thời gian, đếm nhóm sau mỗi thao tác |
| 16 | Cây khung nhỏ nhất | Kruskal (sắp cạnh + DSU), Prim với `heapq` (giới thiệu); cây khung lớn nhất, cạnh lớn nhất nhỏ nhất | Xây đường nối các làng, mạng điện chi phí thấp nhất |

Kiểm tra cuối giai đoạn: đề thi thử nửa chặng (3 bài/150 phút) trộn QHĐ cơ bản và đồ thị, chấm bằng bộ test như thi thật.

## Giai đoạn 5 — QHĐ nâng cao và kết hợp đồ thị + QHĐ (buổi 17–20)

Giai đoạn này nhắm vào bài khó nhất của đề tỉnh; học sinh khá cần làm trọn, học sinh trung bình đặt mục tiêu lấy subtask.

| Buổi | Chủ đề | Nội dung | Bài luyện gợi ý |
| --- | --- | --- | --- |
| 17 | QHĐ trên đoạn | `dp[l][r]` duyệt theo độ dài đoạn; nhân chuỗi ma trận, gộp đá | Gộp các đống sỏi chi phí nhỏ nhất, xâu đối xứng con dài nhất |
| 18 | QHĐ trên DAG & trên đồ thị | QHĐ theo thứ tự tô-pô: đường đi dài nhất, đếm số đường đi; đếm số đường đi ngắn nhất kết hợp Dijkstra | Số cách đi từ 1 đến n với chi phí nhỏ nhất (mod 10^9+7) |
| 19 | QHĐ trên cây | Duyệt cây không đệ quy (BFS lấy thứ tự rồi duyệt ngược); kích thước cây con, tập độc lập lớn nhất trên cây | Chọn nhân viên dự tiệc (không mời cả sếp lẫn cấp dưới), đường kính cây |
| 20 | QHĐ bitmask (n ≤ 15–18) | Biểu diễn tập bằng bit, phân công việc, TSP nhỏ; cảnh báo giới hạn n trong Python | Phân công n người n việc, người giao hàng qua mọi điểm |

Kiểm tra cuối giai đoạn: mỗi học sinh trình bày lại 1 bài kết hợp trước lớp (mô hình hóa → trạng thái → độ phức tạp).

## Giai đoạn 6 — Tổng hợp, thi thử, chiến thuật làm bài (buổi 21–24)

Bốn buổi cuối là thi thử tính giờ bằng đề thật của tỉnh các năm trước, chấm bằng Themis, buổi sau chữa buổi trước.

| Buổi | Nội dung |
| --- | --- |
| 21 | Thi thử đề năm gần nhất (180 phút) + chữa nhanh |
| 22 | Chiến thuật: đọc toàn đề 10 phút, làm subtask trâu trước, viết trâu + sinh test ngẫu nhiên để đối chiếu; thi thử đề thứ hai |
| 23 | Thi thử đề thứ ba; chữa theo lỗi hay gặp (tràn thời gian, sai biên, quên reset, sai tên file) |
| 24 | Ôn tập thư viện code mẫu, đề ngắn khởi động, kiểm tra máy/môi trường Python giống phòng thi |

Chiến thuật chốt cho học sinh: không bỏ trắng bài nào, mỗi bài ít nhất có lời giải vét cạn đúng cho subtask nhỏ.

## Lưu ý riêng cho Python và thư viện code mẫu

Python chậm hơn C++ nhiều lần, nên cùng một thuật toán đúng vẫn có thể mất điểm vì quá thời gian; các quy tắc dưới đây cần trở thành thói quen.

- Luôn đọc toàn bộ input một lần và ghi output một lần.
- Đặt toàn bộ code trong hàm `main()`: biến cục bộ truy cập nhanh hơn biến toàn cục.
- Tránh đệ quy sâu: DFS, duyệt cây, `find` của DSU đều viết bằng vòng lặp.
- Trong vòng lặp nóng, gán `row = dp[i]` rồi dùng `row[j]` thay vì `dp[i][j]`.
- QHĐ mà chỉ cần hàng trước thì giữ 2 hàng, không tạo bảng n×m lớn.
- Nếu phòng thi cho dùng PyPy thì luyện với PyPy từ giữa lộ trình (cần hỏi Sở/đơn vị tổ chức).

### Khung bài thi

```python
import sys

def main():
    data = open('BAI1.INP', 'rb').read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    # ... giải ...
    ans = sum(a)
    with open('BAI1.OUT', 'w') as f:
        f.write(str(ans) + '\n')

main()
```

### BFS

```python
from collections import deque

def bfs(adj, s, n):
    dist = [-1] * (n + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

### Dijkstra

```python
import heapq

def dijkstra(adj, s, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### DSU (không đệ quy)

```python
def make_dsu(n):
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        return True

    return find, union
```

### Duyệt cây không đệ quy (dùng cho QHĐ trên cây)

```python
def tree_order(adj, root, n):
    par = [0] * (n + 1)
    par[root] = -1
    order = []
    stack = [root]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != par[u]:
                par[v] = u
                stack.append(v)
    return order, par  # duyệt reversed(order) để xử lý con trước cha
```
