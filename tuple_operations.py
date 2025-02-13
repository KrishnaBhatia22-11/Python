t = (10, 20, 30, 40, 50)
print(t)

print(t[0], t[-1])

print(t[1:4])

for item in t:
    print(item, end=" ")
print()

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

t4 = t1 * 3
print(t4)

print(20 in t, 100 in t)

packed_tuple = (5, 10, 15)
a, b, c = packed_tuple
print(a, b, c)

nums = (3, 6, 9, 12, 15)
print(len(nums), min(nums), max(nums), sum(nums))

t5 = (2, 3, 4, 2, 2, 5)
print(t5.count(2), t5.index(4))

list_data = [7, 8, 9]
tuple_data = tuple(list_data)
print(tuple_data)

converted_list = list(tuple_data)
print(converted_list)

print("Krishna Bhatia 1/23/SET/BCS/358")
