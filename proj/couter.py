num = input("Enter 10 numbers separated by spaces: ")
numbers = list(map(int, num.split()))
if len(numbers) != 10:
    print("Please enter exactly 10 numbers")
else:
    total = []
    for i in numbers:
        if i % 2 == 0:
            total.append(i)
    count = len(total)
    print(f"There are {count} even numbers in the list.")
    

