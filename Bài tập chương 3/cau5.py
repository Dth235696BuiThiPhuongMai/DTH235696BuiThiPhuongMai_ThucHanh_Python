def test_case(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, " j =", j, " k =", k)
print("Trường hợp a: ")
test_case(3, 5, 7)

print("Trường hợp b: ")
test_case(3, 7, 5)

print("Trường hợp c: ")
test_case(5, 3, 7)

print("Trường hợp d: ")
test_case(5, 7, 3)

print("Trường hợp e: ")
test_case(7, 3, 5)

print("Trường hợp f: ")
test_case(7, 5, 3)