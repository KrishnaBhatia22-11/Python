squares = {x**2 for x in range(1, 11)}
cubes = {x**3 for x in range(1, 11)}

print("Original Squares Set:", squares)
print("Original Cubes Set:", cubes)

squares.update(cubes)
print("After update(cubes):", squares)

removed_element = squares.pop()
print("After pop():", squares)
print("Popped Element:", removed_element)

if 100 in squares:
    squares.remove(100)
    print("After remove(100):", squares)

print("Krishna Bhatia 1/23/SET/BCS/358")
