# Practical : For Statement Programs


# Program 1 : Print Natural Numbers

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(i)


# Program 2 : Print Even Numbers

n = int(input("\nEnter the value of n: "))

for i in range(2, n + 1, 2):
    print(i)


# Program 3 : Print Odd Numbers

n = int(input("\nEnter the value of n: "))

for i in range(1, n + 1, 2):
    print(i)


# Program 4 : Print Powers of 2

n = int(input("\nEnter the value of n: "))

value = 1

for i in range(n):
    print(value)
    value = value * 2


# Program 5 : Sum of Series

n = int(input("\nEnter the value of n: "))

sum = 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)


# Program 6 : Cosine Series

x = float(input("\nEnter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):

    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("Cos(x) =", sum)


# Program 7 : Check Square Root is Prime or Not

import math

number = int(input("\nEnter a Number: "))

root = int(math.sqrt(number))

flag = 0

if root <= 1:
    flag = 1

for i in range(2, root):
    if root % i == 0:
        flag = 1
        break

print("Square Root =", root)

if flag == 0:
    print("Square Root is Prime")
else:
    print("Square Root is Not Prime")


# Program 8 : Pattern

for i in range(3):
    print("A B C")


# Program 9 : Triangle Pattern

n = int(input("\nEnter the value of n: "))

for i in range(1, n + 1):

    for j in range(i):
        print(chr(65 + j), end=" ")

    print()


# Program 10 : Reverse Triangle Pattern

n = int(input("\nEnter the value of n: "))

for i in range(n, 0, -1):

    for j in range(i):
        print(chr(65 + j), end=" ")

    print()


# Program 11 : Number Triangle

n = int(input("\nEnter the value of n: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# Program 12 : Repeated Number Triangle

n = int(input("\nEnter the value of n: "))

for i in range(1, n + 1):

    for j in range(i):
        print(i, end=" ")

    print()
