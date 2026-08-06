# Practical 4
# Set Operations

# 1. Create a Set

fruits = {"Apple", "Banana", "Mango"}

print("Original Set:")
print(fruits)


# 2. Add an Element


fruits.add("Orange")

print("\nAfter Adding Orange:")
print(fruits)


# 3. Union of Two Sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:")
print(set1.union(set2))


# 4. Intersection

print("\nIntersection:")
print(set1.intersection(set2))


# 5. Difference

print("\nDifference:")
print(set1.difference(set2))


# 6. Frozen Set
colors = frozenset({"Red", "Green", "Blue"})

print("\nFrozen Set:")
print(colors)


# 7. Clear a Set

numbers = {10, 20, 30}

print("\nBefore Clear:")
print(numbers)

numbers.clear()

print("After Clear:")
print(numbers)
