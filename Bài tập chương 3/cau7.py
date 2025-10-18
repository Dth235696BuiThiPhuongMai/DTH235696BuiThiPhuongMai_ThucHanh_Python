day = int (input("Nhập vào 1 ngày: ") )
month = int (input("Nhập vào 1 tháng: ") )
year = int (input("Nhập vào 1 năm: ") )

def checkNamNhuan(year):
    if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False    
def checkNgayHopLe(day, month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day >0 and day < 32:
            return True
        else:
            return False
    elif month in (4, 6, 9, 11):
        if day >0 and day < 31:
            return True
        else:
            return False
    elif month == 2:
        if checkNamNhuan(year) == True:
            if day >0 and day < 30:
                return True
            else:
                return False
        else:
            if day >0 and day < 29:
                return True
            else:
                return False
    else:
        return False
while checkNgayHopLe(day, month, year) == False:
    print("Ngày tháng năm không hợp lệ, vui lòng nhập lại")
    day = int (input("Nhập vào 1 ngày: ") )
    month = int (input("Nhập vào 1 tháng: ") )
    year = int (input("Nhập vào 1 năm: ") )
if checkNamNhuan(year) == True:
    if month == 2:
        if day == 29:
            day = 1
            month += 1
        elif day >0 and day < 29:
            day += 1
else:
    if month in (1, 3, 5, 7, 8, 10):
        if day == 31:
            day = 1
            month += 1
        elif day >0 and day < 31:
            day += 1
    elif month in (4, 6, 9, 11):
        if day == 30:
            day = 1
            month += 1
        elif day >0 and day < 30:
            day += 1
    elif month == 12:
        if day == 31:
            day = 1
            month = 1
            year += 1
        elif day >0 and day < 31:
            day += 1
    elif month == 2:
        if day == 28:
            day = 1
            month += 1
        elif day >0 and day < 28:
            day += 1
print("Ngày tiếp theo là: ", day, "/", month, "/", year)