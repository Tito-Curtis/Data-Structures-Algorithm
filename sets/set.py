# 1. creating set in python
firstSet= set((1,2,3))
print(type(firstSet))
# 2. Another way of creating set in python

secondSet={4,5,2,6}
print(secondSet)
print(type(secondSet))

# accessing elements in a set
for i in firstSet:
    print(i)

print(firstSet)

# Adding elements in a set
firstSet.add(23)
firstSet.add((24,50))
print(firstSet)

# removing elements in a set
firstSet.discard(23)
print(firstSet)

# union of set
addset = firstSet.union(secondSet)
print(addset)
add_set = firstSet | secondSet
print(add_set)

# intersection of set
print(firstSet & secondSet)
print(firstSet.intersection(secondSet))
print(firstSet.difference(secondSet))

