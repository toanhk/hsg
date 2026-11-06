# Bồi dưỡng HSG Tin cấp tỉnh — Đồ thị & QHĐ (Python)

Code cho lộ trình 24 buổi trong `lo-trinh-hsg-tin-do-thi-qhd-python.md`.

| Buổi | Chủ đề | Bài trên lớp | Bài về nhà |
| --- | --- | --- | --- |
| 1 | Khung bài thi & I/O nhanh | TONG, CHIA3, BACDINH | MAXMIN, LUOI, TANSUAT |
| 2 | Độ phức tạp & CTDL sẵn có | TONGDOAN, CAPK, DEMKHOANG | HANGDOI, NOIDAY, DOANK |
| 3 | Đệ quy & quay lui | XAUNP, TOHOP, TAPCON | HOANVI, QUANHAU, DIENDAU |
| 4 | Từ đệ quy đến QHĐ | FIBO, CAUTHANG, DOITIEN | CATGO, DEMXAU, VE1 |
| 5 | QHĐ một chiều | KHONGKE, DOANMAX, TORAO | ECHNHAY, COPHIEU, XOA1 |
| 6 | Cái túi | TUI01, TUIVOHAN, TRUYVET | CHIAKEO, DOITIEN2, TUILON |
| 7 | Dãy con: LIS, LCS, sửa xâu | LIS, LCS, SUAXAU | DOIXUNG, TENLUA, THAPHOP |
| 8 | QHĐ trên lưới | DUONGDI, DEMDUONG, HINHVUONG | VANG, HVCON, HAIROBOT |
| 10 | DFS & liên thông | LIENTHONG, CHUTRINH, HAIPHIA | NHOMBAN, HAIPHE, CHIADOI |

Kiểm tra cuối giai đoạn 2 (120 phút): `kiemtra_gd2/` gồm MUAVE, BALO, NUI.

Mỗi thư mục `sessionNN/` có `loi_giai/` (lời giải chính + bản vét cạn `_trau`), `sinh_test.py`
(sinh test theo cấu trúc Themis `test/BAI/TestNN/`), `cham_thu.py` và `template.py`.
Từ buổi 6, bài có nhiều đáp án đúng (TRUYVET) được chấm bằng hàm cùng tên trong `kiem_tra.py`.

```
cd session03
python sinh_test.py           # sinh test cho cả 6 bài
python cham_thu.py TAPCON     # chấm loi_giai/TAPCON.py
python cham_thu.py TAPCON loi_giai/TAPCON_trau.py
```
