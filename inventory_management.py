inventory = input("Enter items in inventory (comma separated): ").split(", ")

item_to_add = input("Enter item to add: ")
inventory.append(item_to_add)
print("After adding:", inventory)

item_to_remove = input("Enter item to remove: ")
for i in range(len(inventory)):
    if inventory[i] == item_to_remove:
        del inventory[i]
        break

print("After removing:", inventory)
print("Krishna Bhatia 1/23/SET/BCS/358")
