s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print("Set s1:", s1)
print("Set s2:", s2)

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Difference (s2 - s1):", s2 - s1)
print("Symmetric Difference:", s1 ^ s2)

s3 = {2, 4, 6, 8, 10}
print("Set s3:", s3)

print("Common elements in s1, s2, s3:", s1 & s2 & s3)

fs3 = frozenset(s3)
print("Frozen set s3:", fs3)

print("Krishna Bhatia 1/23/SET/BCS/358")
