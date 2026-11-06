# Bồi dưỡng HSG Tin cấp tỉnh — Đồ thị & QHĐ (Python)

Code cho lộ trình 24 buổi trong `lo-trinh-hsg-tin-do-thi-qhd-python.md`.

| Buổi | Chủ đề | Bài trên lớp | Bài về nhà |
| --- | --- | --- | --- |
| 1 | Khung bài thi & I/O nhanh | TONG, CHIA3, BACDINH | MAXMIN, LUOI, TANSUAT |
| 2 | Độ phức tạp & CTDL sẵn có | TONGDOAN, CAPK, DEMKHOANG | HANGDOI, NOIDAY, DOANK |
| 3 | Đệ quy & quay lui | XAUNP, TOHOP, TAPCON | HOANVI, QUANHAU, DIENDAU |
| 4 | Từ đệ quy đến QHĐ | FIBO, CAUTHANG, DOITIEN | CATGO, DEMXAU, VE1 |
| 7 | Dãy con: LIS, LCS, sửa xâu | LIS, LCS, SUAXAU | DOIXUNG, TENLUA, THAPHOP |

Mỗi thư mục `buoiNN/` có `loi_giai/` (lời giải chính + bản vét cạn `_trau`), `sinh_test.py`
(sinh test theo cấu trúc Themis `test/BAI/TestNN/`), `cham_thu.py` và `template.py`.

```
cd buoi03
python sinh_test.py           # sinh test cho cả 6 bài
python cham_thu.py TAPCON     # chấm loi_giai/TAPCON.py
python cham_thu.py TAPCON loi_giai/TAPCON_trau.py
```
