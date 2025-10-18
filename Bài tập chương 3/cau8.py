def tinhGiaTri(x, n, toanTu):
    giaTri = 0
    if toanTu == "+":
       giaTri =float( x + n)
    elif toanTu == "-":
       giaTri = float( x - n)
    elif toanTu == "*":
       giaTri = float( x * n)
    elif toanTu == "/":
       while n==0:
             print("Khong the chia cho 0, vui long nhap lai so thu hai!")
             n = float(input("Nhap vao so thu hai: "))
             giaTri = float( x / n) 
       else:
            giaTri = float ( x / n)
    return giaTri
print("Nhap vao mot bieu thuc: ")
a = float(input("Nhap vao so thu nhat: "))
b = input("Nhap vao toan tu (+, -, *, /): ")
c = float(input("Nhap vao so thu hai: "))
print("Ket qua cua bieu thuc ", a, b, c, " la: ", tinhGiaTri(a, c, b))
