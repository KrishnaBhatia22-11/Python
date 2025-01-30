import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are: {root1:.2f} and {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root is: {root:.2f}")
else:
    print("No real roots, the roots are imaginary.")
print("Krishna Bhatia 1/23/SET/BCS/358")
