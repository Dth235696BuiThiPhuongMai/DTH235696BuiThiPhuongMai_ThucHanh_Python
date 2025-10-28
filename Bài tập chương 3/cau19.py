def GiaiThua(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * GiaiThua(a-1)
def TinhGiaTriBieuThuc(x, n):
    tong = 0
    for i in range(n+1):
        m = 2*i+1
        GT = x**m / GiaiThua(m)
        tong += GT
    return tong
x = float(input("Nhập vào giá trị x: "))
n = int(input("Nhập vào giá trị n: "))
'''while n < 1:
    print("Giá trị n không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập vào giá trị n (n => 1): "))'''
print("Giá trị của biểu thức S =", TinhGiaTriBieuThuc(x, n))