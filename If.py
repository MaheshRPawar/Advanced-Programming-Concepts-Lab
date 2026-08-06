# Practical : If Statement Programs

# Program 1 : Check Zero or Non-Zero

number = int(input("Enter a number: "))

if number == 0:
    print("The number is Zero.")
else:
    print("The number is Non-Zero.")


# Program 2 : Largest of Two Numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1 > num2:
    print("Largest Number =", num1)
else:
    print("Largest Number =", num2)


# Program 3 : Check Positive or Negative

number = int(input("Enter a Number: "))

if number >= 0:
    print("The number is Positive.")
else:
    print("The number is Negative.")


# Program 4 : Check Vowel or Consonant

character = input("Enter a Character: ")

if character in "aeiouAEIOU":
    print("It is a Vowel.")
else:
    print("It is a Consonant.")


# Program 5 : Student Performance

percentage = float(input("Enter Percentage: "))

if percentage >= 90:
    print("Excellent Performance")
elif percentage >= 80:
    print("Very Good Performance")
elif percentage >= 70:
    print("Good Performance")
elif percentage >= 60:
    print("Average Performance")
else:
    print("Poor Performance")


# Program 6 : Largest of Three Numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest Number =", num2)
else:
    print("Largest Number =", num3)


# Program 7 : Smallest of Three Numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 <= num2 and num1 <= num3:
    print("Smallest Number =", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest Number =", num2)
else:
    print("Smallest Number =", num3)


# Program 8 : Check Even or Odd

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Program 9 : Check Leap Year

year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")


# Program 10 : Driver Insurance

status = input("Married or Unmarried (M/U): ").upper()

if status == "M":
    print("Driver is Insured.")
else:
    gender = input("Enter Gender (M/F): ").upper()
    age = int(input("Enter Age: "))

    if gender == "M" and age > 30:
        print("Driver is Insured.")
    elif gender == "F" and age > 25:
        print("Driver is Insured.")
    else:
        print("Driver is Not Insured.")
