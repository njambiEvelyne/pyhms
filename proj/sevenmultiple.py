print("Multiples of 7 from 1 to 50:")
print("-" * 30)

for i in range(1, 51):  # Changed to 51 to include 50 if needed
    if i % 7 == 0:
        result = i / 7
        print(f"{i} is divisible by 7 → {i} ÷ 7 = {result}")