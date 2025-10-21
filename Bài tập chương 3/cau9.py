month = int (input("Nhập vào 1 tháng: "))
while month < 1 or month > 12:
    print("Tháng không hợp lệ, vui lòng nhập lại!")
    month = int (input("Nhập vào 1 tháng: "))
    if month in (1, 2, 3):
        print("Tháng vừa nhập thuộc Quý 1")
    elif month in (4, 5, 6):
        print("Tháng vừa nhập thuộc Quý 2")
    elif month in (7, 8, 9):
        print("Tháng vừa nhập thuộc Quý 3")
    else:
        print("Tháng vừa nhập thuộc Quý 4")




