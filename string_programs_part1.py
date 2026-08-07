# Program 1 : Find String Length

text = input("Enter a string: ")

count = 0

for ch in text:
    count = count + 1

print("Length of String =", count)


# Program 2 : Count Vowels, Consonants, Digits, Spaces and Special Characters

text = input("\nEnter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in text:

    if ch in "AEIOUaeiou":
        vowels = vowels + 1

    elif ch.isalpha():
        consonants = consonants + 1

    elif ch.isdigit():
        digits = digits + 1

    elif ch == " ":
        spaces = spaces + 1

    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


# Program 3 : Reverse a String

text = input("\nEnter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reverse String =", reverse)


# Program 4 : Check Palindrome

text = input("\nEnter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Program 5 : Count Uppercase and Lowercase Letters

text = input("\nEnter a string: ")

upper = 0
lower = 0

for ch in text:

    if ch.isupper():
        upper = upper + 1

    elif ch.islower():
        lower = lower + 1

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)


# Program 6 : Replace Characters

text = input("\nEnter a string: ")

old = input("Enter character to replace: ")

new = input("Enter new character: ")

result = ""

for ch in text:

    if ch == old:
        result = result + new
    else:
        result = result + ch

print("Updated String =", result)


# Program 7 : Remove Spaces

text = input("\nEnter a string: ")

result = ""

for ch in text:

    if ch != " ":
        result = result + ch

print("String without Spaces =", result)


# Program 8 : Frequency of a Character

text = input("\nEnter a string: ")

character = input("Enter character: ")

count = 0

for ch in text:

    if ch == character:
        count = count + 1

print("Frequency =", count)


# Program 9 : First and Last Character

text = input("\nEnter a string: ")

print("First Character =", text[0])

print("Last Character =", text[-1])


# Program 10 : Display ASCII Values

text = input("\nEnter a string: ")

for ch in text:

    print(ch, "=", ord(ch))
