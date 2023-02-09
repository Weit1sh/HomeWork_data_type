print("Enter the size in kilobaitas")
size = int(input(">>> "))
baitas = size * 1024
page = 30 * 40
x = baitas / page
x = round(x, 2)
print("This document takes " + str(x) + " pages!")
