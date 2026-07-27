# Array

from array import *

# Number Array
arr = array('i', [10, 20, 30, 40])
print(arr)

# Index
print(arr[0])
print(arr[1])
print(arr[2])

# Append
arr.append(50)
print(arr)

# Insert
arr.insert(2, 25)
print(arr)

# Remove
arr.remove(40)
print(arr)

# Pop
arr.pop()
print(arr)

# Reverse
arr.reverse()
print(arr)

# Length
print(len(arr))

# Loop
for i in arr:
    print(i)
