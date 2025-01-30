numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for num in numbers:
    if num % 2 != 0:
        continue
    print(f"First even number is: {num}")
    break
print("Krishna Bhatia 1/23/SET/BCS/358")
