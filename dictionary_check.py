data = {"name": "KRISHNA", "age": 25, "city": "FARIDABAD"}

key = input("Enter the key to check: ")

if key in data:
    print("Key exists. Value:", data[key])
else:
    print("Key does not exist.")
    value = input("Enter value for the new key: ")
    data[key] = value
    print("Updated Dictionary:", data)

print("Krishna Bhatia 1/23/SET/BCS/358")
