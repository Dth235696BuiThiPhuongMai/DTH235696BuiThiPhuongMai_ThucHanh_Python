def Doc_so(n):
    Hang_chuc = [" ", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    Hang_don_vi = [" ", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 10:
        return Hang_don_vi[n]
    else:
        chuc = n // 10
        don_vi = n % 10
        if don_vi ==0:
            return Hang_chuc[chuc]
        else:
            return Hang_chuc[chuc] + " " + Hang_don_vi[don_vi]

while True:
    n = int(input("Nhap mot so nguyen 2 chu so: "))
    if n>9 and n<100:
        break
    else:
      print("Nhap sai, vui long nhap lai")
print("So nguyen ", n, " doc la: ", Doc_so(n))