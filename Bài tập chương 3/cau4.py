x, y, z = 3, 5, 7

print("(a)", x == 3)          # True vì x = 3
print("(b)", x < y)           # True vì 3 < 5
print("(c)", x >= y)          # False vì 3 >= 5 sai
print("(d)", x <= y)          # True vì 3 <= 5
print("(e)", x != y - 2)      # False vì 3 != 3 sai
print("(f)", x < 10)          # True vì 3 < 10
print("(g)", x >= 0 and x < 10)  # True vì cả 2 điều kiện đúng
print("(h)", x < 0 and x < 10)   # False vì x < 0 sai
print("(i)", x >= 0 and x < 2)   # False vì x < 2 sai
print("(j)", x < 0 or x < 10)    # True vì x < 10 đúng
print("(k)", x > 0 or x < 10)    # True vì x > 0 đúng
print("(l)", x < 0 or x > 10)    # False vì cả 2 điều kiện sai