import math
x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between two points:", distance)
print("Krishna Bhatia 1/23/SET/BCS/358")
