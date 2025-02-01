num_list = input("Enter list of numbers (comma separated): ").split(", ")
num_list = [int(num) for num in num_list]
is_palindrome = True

for i in range(len(num_list) // 2):
    if num_list[i] != num_list[len(num_list) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

print("Krishna Bhatia 1/23/SET/BCS/358")
