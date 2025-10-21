while True:
    n = int (input("Nhập vào một số nguyên dương n: "))
    if n<1 :
        print("Số vừa nhập không phải số nguyên tố. ")
    else:
        dem = 0
        for i in range(1,n+1):
            if n%i==0:
                dem+=1
        if dem==2:
            print(n," là số nguyên tố.")
        else:
            print(n,"Không phải số nguyên tố.")
        hoi = input("Bạn có muốn tiếp tục không? (c/k)")
        if hoi =="k":
            break
print("Chương trình kết thúc.")
        
         
             

