# Accept inputs
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = complex(input("Enter a complex number (e.g., 2+3j): "))

# Perform operations
sum_result = a + b + c
mul_result = a * b * c

# Print results
print("Sum:", sum_result, "Type:", type(sum_result))
print("Multiplication:", mul_result, "Type:", type(mul_result))
