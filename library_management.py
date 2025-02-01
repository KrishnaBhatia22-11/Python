books = input("Enter books in library (comma separated): ").split(", ")

book_to_add = input("Enter book to add: ")
books.append(book_to_add)
print("Books after adding:", books)

book_to_remove = input("Enter book to remove: ")
for i in range(len(books)):
    if books[i] == book_to_remove:
        del books[i]
        break

print("Books after removing:", books)

search = input("Enter book to search for: ")
found = False
for book in books:
    if book == search:
        found = True
        break

if found:
    print(search, "is available")
else:
    print(search, "is not available")

print("Krishna Bhatia 1/23/SET/BCS/358")
