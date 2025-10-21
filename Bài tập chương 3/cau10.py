def GiaiThua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * GiaiThua(n - 1)
def TinhGiaTriBieuThuc(x, n):
    tong = 0
    for i in range(1, n+1):
        GT = x**i / GiaiThua(i)
        tong += GT
    return tong
x = float(input("Nhập vào giá trị x: "))
n = int(input("Nhập vào giá trị n (n > 1): "))
while n <= 1:
    print("Giá trị n không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập vào giá trị n (n > 1): "))
print("Giá trị của biểu thức S =", TinhGiaTriBieuThuc(x, n))