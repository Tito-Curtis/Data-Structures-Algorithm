# mutable
# key-Value pairs

# creating dictionary
books = {1:"intro",2:"calculus",3:"physics"}
print(type(books))
print(books)

# accessing dictionary element
print(books[2])
print(books.get(1))

# changing and adding dictionary element
books[2] ="statistics"
books[4] = "database"
print(books)

print(books.keys())
print(books.values())
print(books.items())