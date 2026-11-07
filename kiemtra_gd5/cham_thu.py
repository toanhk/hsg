# CHAM THU tren may (thay Themis khi luyen o nha)
# Chay: python cham_thu.py TONG   -> chay loi_giai/TONG.py tren moi test, bao dung/sai va thoi gian
# Buoi 6: bai co NHIEU dap an dung (TRUYVET) duoc cham bang ham trong kiem_tra.py thay vi so tung tu.
import os, shutil, subprocess, sys, time, tempfile

try:
    import kiem_tra                      # kiem_tra.py dat canh file nay (khong co cung khong sao)
except ImportError:
    kiem_tra = None

def main():
    bai = sys.argv[1]
    code = sys.argv[2] if len(sys.argv) > 2 else os.path.join('loi_giai', bai + '.py')
    code = os.path.abspath(code)
    goc = os.path.join('test', bai)
    kt = getattr(kiem_tra, bai, None) if kiem_tra else None
    tong_diem = 0
    ds = sorted(os.listdir(goc))
    for t in ds:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(os.path.join(goc, t, bai + '.INP'), tmp)
            bat_dau = time.perf_counter()
            try:
                subprocess.run([sys.executable, code], cwd=tmp, timeout=5, check=True)
                tg = time.perf_counter() - bat_dau
                ra = open(os.path.join(tmp, bai + '.OUT')).read()
                dap_an = open(os.path.join(goc, t, bai + '.OUT')).read()
                if kt:
                    dung = kt(open(os.path.join(goc, t, bai + '.INP')).read(), dap_an, ra)
                else:
                    dung = ra.split() == dap_an.split()
                kq = 'DUNG' if dung else 'SAI'
                if tg > 1.0:
                    kq += ' nhung QUA 1 GIAY'
                elif dung:
                    tong_diem += 1
            except subprocess.TimeoutExpired:
                tg, kq = 5.0, 'QUA THOI GIAN'
            except Exception as loi:
                tg, kq = 0.0, 'LOI: ' + type(loi).__name__
        print(f'{t}: {kq:22s} {tg:.2f} s')
    print(f'Diem: {tong_diem}/{len(ds)} test')

main()
