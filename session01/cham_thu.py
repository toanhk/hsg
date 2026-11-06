# CHAM THU tren may (thay Themis khi luyen o nha)
# Chay: python cham_thu.py TONG   -> chay loi_giai/TONG.py tren moi test, bao dung/sai va thoi gian
import os, shutil, subprocess, sys, time, tempfile

def main():
    bai = sys.argv[1]
    code = sys.argv[2] if len(sys.argv) > 2 else os.path.join('loi_giai', bai + '.py')
    code = os.path.abspath(code)
    goc = os.path.join('test', bai)
    tong_diem = 0
    ds = sorted(os.listdir(goc))
    for t in ds:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(os.path.join(goc, t, bai + '.INP'), tmp)
            bat_dau = time.perf_counter()
            try:
                subprocess.run([sys.executable, code], cwd=tmp, timeout=5, check=True)
                tg = time.perf_counter() - bat_dau
                ra = open(os.path.join(tmp, bai + '.OUT')).read().split()
                dung = ra == open(os.path.join(goc, t, bai + '.OUT')).read().split()
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
