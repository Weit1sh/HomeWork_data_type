print("Enter the symbol")
small = input(">>> ")


name = "abcdefghigklmnopqrstuvwxyz"
a = name.find(small)
print("Symbol position is " + str(a + 1))


print("Enter symbol position")
big = int(input(">>> "))


nam_1 = "ABCDEFGHIJKLMNOPQRSTUVWZYX"
b = name[big - 1]
print("This is " + b.upper())
