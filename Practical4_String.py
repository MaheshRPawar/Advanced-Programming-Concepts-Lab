# Practical 4
# String Operations


# 1. Create a String

text = "Welcome to Python"

print("Original String:")
print(text)



# 2. Access Characters

print("\nFirst Character :", text[0])
print("Last Character :", text[-1])



# 3. String Slicing

print("\nFirst 7 Characters :", text[:7])
print("Characters from Index 8 :", text[8:])
print("Characters from Index 2 to 8 :", text[2:9])



# 4. Reverse String

print("\nReverse String :")
print(text[::-1])


# 5. Update String

text = "Python Programming"

print("\nUpdated String :")
print(text)


# 6. String Formatting

name = "Rahul"
branch = "CSE"

print("\nStudent Name :", name)
print("Branch :", branch)

print("My name is {} and I study in {}.".format(name, branch))
