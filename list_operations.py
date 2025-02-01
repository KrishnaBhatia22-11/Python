my_list = [1, 2, 3, 4, 5]

print("First element:", my_list[0])

my_list[0] = 10
print("Modified list:", my_list)

my_list.append(6)
print("List after adding 6:", my_list)

my_list.extend([7, 8])
print("List after adding 7 and 8:", my_list)

my_list.remove(10)
print("List after removing 10:", my_list)

del my_list[0]
print("List after removing first element:", my_list)

print("Elements from 2nd to 4th:", my_list[1:4])

my_list.sort()
print("Sorted list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

new_list = my_list + [10, 11, 12]
print("Concatenated list:", new_list)

print("Sorted concatenated list:", sorted(new_list))

print("Krishna Bhatia 1/23/SET/BCS/358")
