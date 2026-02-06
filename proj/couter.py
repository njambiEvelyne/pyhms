num = int(input("Enter 10 numbers: "))
for i in num:
  total = []
  if i % 2 == 0:
    total.append(i)
    count = len(total)
print(f"There are {count} even numbers in the list.")
    

