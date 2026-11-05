# TONG - ban CHAM kieu hoc sinh hay viet: input() tung dong, print ket qua
# Van dung, nhung cham hon ban doc nhanh; dung de so sanh tren lop.
import sys
sys.stdin = open('TONG.INP')
sys.stdout = open('TONG.OUT', 'w')
n = int(input())
tong = 0
chan = 0
for i in range(n):
    x = int(input())
    tong += x
    if x % 2 == 0:
        chan += 1
print(tong)
print(chan)
