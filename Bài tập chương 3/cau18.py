#Hinh vuong roongx

n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
#Hinh tam giac

n = 4
for i in range(1, n + 1):
    print(" " * (n - i) , "*" * i)
        

#Hinh loop
#n = int(input("Nhap n: "))
n = 7
for i in range(n):
    for j in range(n): 
        if i == j or i == n//2 or (j==0 and i<n//2) or (j==n-1 and i>n//2) :
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    


   

       
        




          
    


