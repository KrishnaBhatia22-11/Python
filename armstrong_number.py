num = int(input("Enter a number: "))
sum_of_digits = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** digits
    temp //= 10

if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
print("Krishna Bhatia 1/23/SET/BCS/358")
