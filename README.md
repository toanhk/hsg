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
| 9 | Biểu diễn đồ thị & BFS | THANHPHO, LOTRINH, BIENSO | MAKHOA, DUONGTD, DEMNGAN |
| 10 | DFS & liên thông | LIENTHONG, CHUTRINH, HAIPHIA | NHOMBAN, HAIPHE, CHIADOI |
| 11 | Loang trên lưới | DEMDAO, MECUNG, LUALAN | HONUOC, QUANMA, CHAYTHOAT |
| 12 | Sắp xếp tô-pô | MONHOC, TIMVONG, SOHOCKY | CONGVIEC, TUDIEN, DINHHUONG |
| 13 | Dijkstra | KHOANGCACH, HANHTRINH, QUATRAM | BENHVIEN, SUADUONG, TAUHOA |
| 14 | Biến thể đường đi | DAOCHIEU, MIENPHI, MOICAP | GIAMGIA, MOTUYEN, THUONGPHAT |
| 15 | DSU (Disjoint Set Union) | KETBAN, DEMNHOM, QUYNHOM | DAONOI, CATDIEN, SONHANG |
| 16 | Cây khung nhỏ nhất | NOILANG, DOCTHAP, MANGDIEN | GIACOCAU, CHENHLECH, XETAI |
| 17 | QHĐ trên đoạn | GOPSOI, NHANMT, LAYSO | CATDX, BANBONG, DAYNGOAC |
| 18 | QHĐ trên DAG & trên đồ thị | DUONGDAI, DEMLOTRINH, DUONGRE | TRUOTTUYET, THANGTHUA, CHUYENBAY |
| 19 | QHĐ trên cây | CAYCON, DUTIEC, DUONGKINH | CATCANH, TONGKC, TIENQUYET |
| 20 | QHĐ bitmask (n ≤ 15–20) | PHANCONG, COMBO, GIAOHANG | GHEPCAP, KHOBAU, LICHHOC |
| 21 | Thi thử đề thật Ninh Bình 2023-2024 (06/10/2023) | PAIRCOUNT, KPRIMESUB, ST25 | SEQ, RBGAME (đề 07/10/2023) |
| 22 | Chiến thuật, trâu + đối chiếu; thi thử số 2 | TRAMSAC, LEONUI, XEPLICH | |
| 23 | Thi thử số 3, chữa theo lỗi hay gặp | TONGCON, GIOHANG, PHATUONG | |
| 24 | Đề khởi động, thư viện code mẫu, kiểm tra máy | SONT, NOIMANG, LATGACH | |

Kiểm tra cuối giai đoạn 2 (120 phút): `kiemtra_gd2/` gồm MUAVE, BALO, NUI.
Kiểm tra cuối giai đoạn 3 (120 phút): `kiemtra_gd3/` gồm XEPHANG, CUUHOA (lưới 1000×1000), TRUNGCHUYEN.
Kiểm tra cuối giai đoạn 4 (thi thử nửa chặng, 150 phút): `kiemtra_gd4/` gồm DONGHANG (QHĐ), CHONTUYEN (Dijkstra), PHANCUM (cây khung đồ thị dày).
Kiểm tra cuối giai đoạn 5 (bài kết hợp đồ thị + QHĐ, 150 phút, kèm hướng dẫn trình bày): `kiemtra_gd5/` gồm GIAMSAT (QHĐ trên cây 3 trạng thái), NGAMCANH (Dijkstra + QHĐ trên DAG đường ngắn nhất), MUASAM (nhiều lần Dijkstra + QHĐ bitmask).
Buổi 20 có `do_bitmask.py` đo giới hạn n với Python: 2^n·n chỉ an toàn tới n = 18, TSP 2^n·n² tới n = 16.

Giai đoạn 6 (buổi 21–24): đề thật lấy từ `De_24_THPT.docx` (bộ test tự sinh theo đúng ràng buộc, không phải test chính thức).
`session22/doi_chieu.py` + `sinh_nho/` đối chiếu lời giải với trâu trên test ngẫu nhiên nhỏ;
`session23/soat_bai.py` soát lỗi hình thức (tên file, input(), đệ quy) trước khi nộp, các bản lỗi `_sai`, `_quenreset`, `_bang`;
`session24/thu_vien/` là thư viện code mẫu (đồ thị, QHĐ, số học) kèm `kiem_thu_thu_vien.py`, `session24/kiem_tra_may.py` đo hệ số chậm của máy thi.

Mỗi thư mục `sessionNN/` có `loi_giai/` (lời giải chính + bản vét cạn `_trau`), `sinh_test.py`
(sinh test theo cấu trúc Themis `test/BAI/TestNN/`), `cham_thu.py` và `template.py`.
Từ buổi 6, bài có nhiều đáp án đúng (TRUYVET, LOTRINH; buổi 12: MONHOC, TIMVONG, DINHHUONG; buổi 13: HANHTRINH) được chấm bằng hàm cùng tên trong `kiem_tra.py`.

```
cd session03
python sinh_test.py           # sinh test cho cả 6 bài
python cham_thu.py TAPCON     # chấm loi_giai/TAPCON.py
python cham_thu.py TAPCON loi_giai/TAPCON_trau.py
```
