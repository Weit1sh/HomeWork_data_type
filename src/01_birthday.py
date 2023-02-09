print("Enter the day")
day = int(input(">>> "))
print("Enter the month")
month = int(input(">>> "))

if 0 > day or day >= 32:
    print("You're joking")
    exit()
elif 0 > month or month >= 13:
    print("You're joking")
    exit()


print("Your birthday in the year takes " + str((30 * month) + day) + " day!")
