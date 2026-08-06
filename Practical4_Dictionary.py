# Practical 4
# Dictionary Operations

# 1. Create a Dictionary

student = {
    "Roll No": 1,
    "Name": "Rahul",
    "Branch": "CSE"
}

print("Student Details:")
print(student)


# 2. Access a Value
print("\nStudent Name:")
print(student["Name"])


# 3. Add a New Item
student["City"] = "Kolhapur"

print("\nAfter Adding City:")
print(student)


# 4. Update a Value

student["Branch"] = "Computer Science"

print("\nAfter Updating Branch:")
print(student)


# 5. Delete a Value

del student["City"]

print("\nAfter Deleting City:")
print(student)

# 6. Dictionary Methods

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\nTotal Items:")
print(len(student))
