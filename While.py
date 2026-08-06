# Practical : While Statement Programs

# Program 1 : Print Natural Numbers

n = int(input("Enter the value of n: "))

i = 1

while i <= n:
    print(i)
    i = i + 1


# Program 2 : Print Even Numbers

n = int(input("\nEnter the value of n: "))

i = 2

while i <= n:
    print(i)
    i = i + 2


# Program 3 : Print Odd Numbers

n = int(input("\nEnter the value of n: "))

i = 1

while i <= n:
    print(i)
    i = i + 2


# Program 4 : Sum of Natural Numbers

n = int(input("\nEnter the value of n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


# Program 5 : Sum of Odd Numbers

n = int(input("\nEnter the value of n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)


# Program 6 : Sum of Even Numbers

n = int(input("\nEnter the value of n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)


# Program 7 : Natural Numbers in Reverse Order

n = int(input("\nEnter the value of n: "))

while n >= 1:
    print(n)
    n = n - 1


# Program 8 : Fibonacci Series

n = int(input("\nEnter the number of terms: "))

first = 0
second = 1
count = 1

while count <= n:
    print(first, end=" ")
    next = first + second
    first = second
    second = next
    count = count + 1


# Program 9 : Factorial of a Number

number = int(input("\nEnter a number: "))

fact = 1

while number > 0:
    fact = fact * number
    number = number - 1

print("Factorial =", fact)


# Program 10 : Check Prime Number

number = int(input("\nEnter a number: "))

i = 2
flag = 0

while i < number:
    if number % i == 0:
        flag = 1
        break
    i = i + 1

if number <= 1:
    print("Not Prime")
elif flag == 0:
    print("Prime Number")
else:
    print("Not Prime")


# Program 11 : Sum of Digits

number = int(input("\nEnter a number: "))

sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print("Sum of Digits =", sum)


# Program 12 : Check Palindrome Number

number = int(input("\nEnter a number: "))

temp = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if temp == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome")


# Program 13 : Reverse a Number

number = int(input("\nEnter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse Number =", reverse)


# Program 14 : Multiplication Table

number = int(input("\nEnter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1


# Program 15 : Largest of n Numbers

count = int(input("\nHow many numbers? "))

i = 1

largest = None

while i <= count:
    number = int(input("Enter Number: "))

    if largest is None or number > largest:
        largest = number

    i = i + 1

print("Largest Number =", largest)


# Program 16 : Smallest of n Numbers

count = int(input("\nHow many numbers? "))

i = 1

smallest = None

while i <= count:
    number = int(input("Enter Number: "))

    if smallest is None or number < smallest:
        smallest = number

    i = i + 1

print("Smallest Number =", smallest)
