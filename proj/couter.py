num = int(input("Enter 10 numbers: "))
for i in num:
    if i % 2 == 0:
        print(f"{i} is an even number.")
    elif i % 2 != 0:  
        print(f"{i} is an odd number.")
