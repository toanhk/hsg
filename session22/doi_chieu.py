# DOI CHIEU (stress test): sinh test NHO ngau nhien, chay loi giai can kiem tra va ban vet can (trau),
# so ket qua. Gap test khac nhau thi dung lai, luu test vao loi/BAI.INP de mo ra xem va sua.
# Chay:  python doi_chieu.py TRAMSAC                                 (mac dinh: loi_giai/TRAMSAC.py vs _trau)
#        python doi_chieu.py TRAMSAC loi_giai/TRAMSAC_thamlam.py      (kiem tra ban khac voi trau)
#        python doi_chieu.py TRAMSAC loi_giai/TRAMSAC_thamlam.py 500  (so lan thu, mac dinh 200)
# Can co: sinh_nho/BAI.py nhan mot so "hat giong" tren dong lenh va in ra MOT test nho (ra man hinh).
# Quy trinh trong phong thi (buoi 22):
#   1) Viet trau truoc (vet can, chac chan dung) -> nop ngay de giu diem subtask nho.
#   2) Viet sinh test nho (n <= 8..15) - chi 10 dong.
#   3) Viet loi giai nhanh, chay doi_chieu vai tram lan. Khac nhau -> co test nho de do tay.
import os, shutil, subprocess, sys, tempfile

def chay(code, bai, inp):
    """Chay file code trong thu muc tam co BAI.INP, tra ve noi dung BAI.OUT (hoac thong bao loi)."""
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, bai + '.INP'), 'w') as f:
            f.write(inp)
        try:
            r = subprocess.run([sys.executable, code], cwd=tmp, timeout=10, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            return 'QUA THOI GIAN'
        if r.returncode != 0:
            return 'LOI CHAY:\n' + r.stderr[-600:]
        try:
            return open(os.path.join(tmp, bai + '.OUT')).read()
        except FileNotFoundError:
            return 'KHONG CO FILE ' + bai + '.OUT (sai ten file?)'

def main():
    bai = sys.argv[1]
    nhanh = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.join('loi_giai', bai + '.py'))
    trau = os.path.abspath(os.path.join('loi_giai', bai + '_trau.py'))
    sinh = os.path.abspath(os.path.join('sinh_nho', bai + '.py'))
    so_lan = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    for lan in range(1, so_lan + 1):
        inp = subprocess.run([sys.executable, sinh, str(lan)], capture_output=True, text=True, check=True).stdout
        a = chay(nhanh, bai, inp)
        b = chay(trau, bai, inp)
        if a.split() != b.split():
            os.makedirs('loi', exist_ok=True)
            with open(os.path.join('loi', bai + '.INP'), 'w') as f:
                f.write(inp)
            print(f'KHAC NHAU o lan thu {lan} (hat giong {lan}). Test da luu vao loi/{bai}.INP')
            print('--- Input ---'); print(inp.rstrip())
            print('--- Loi giai ---'); print(a.rstrip())
            print('--- Trau ---'); print(b.rstrip())
            return
        if lan % 50 == 0:
            print(f'  ... {lan} test giong nhau')
    print(f'OK: {so_lan} test ngau nhien deu giong trau')

main()
