# Program 21 : Password Validator

password = input("Enter Password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")


# Program 22 : Run-Length Encoding

text = input("\nEnter a String: ")

count = 1

for i in range(len(text)):

    if i == len(text) - 1:
        print(text[i] + str(count), end="")

    elif text[i] == text[i + 1]:
        count = count + 1

    else:
        print(text[i] + str(count), end="")
        count = 1

print()


# Program 23 : String Compression

text = input("\nEnter a String: ")

result = ""
count = 1

for i in range(len(text)):

    if i == len(text) - 1:
        result = result + text[i] + str(count)

    elif text[i] == text[i + 1]:
        count = count + 1

    else:
        result = result + text[i] + str(count)
        count = 1

if len(result) < len(text):
    print("Compressed String =", result)
else:
    print("Compressed String =", text)


# Program 24 : Most Frequent Character

text = input("\nEnter a String: ")

maximum = 0
character = ""

for ch in text:

    if text.count(ch) > maximum:
        maximum = text.count(ch)
        character = ch

print("Most Frequent Character =", character)


# Program 25 : Second Most Frequent Character

text = input("\nEnter a String: ")

frequency = {}

for ch in text:
    frequency[ch] = text.count(ch)

values = list(set(frequency.values()))
values.sort(reverse=True)

if len(values) >= 2:

    second = values[1]

    for ch in frequency:
        if frequency[ch] == second:
            print("Second Most Frequent Character =", ch)
            break
else:
    print("Second Most Frequent Character Not Found")


# Program 26 : Caesar Cipher

text = input("\nEnter a String: ")

shift = int(input("Enter Shift Value: "))

result = ""

for ch in text:

    if ch.isalpha():

        if ch.isupper():
            result = result + chr((ord(ch) - 65 + shift) % 26 + 65)

        else:
            result = result + chr((ord(ch) - 97 + shift) % 26 + 97)

    else:
        result = result + ch

print("Encrypted String =", result)


# Program 27 : Email Validator

email = input("\nEnter Email Address: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# Program 28 : Word Frequency Dictionary

text = input("\nEnter a Paragraph: ")

words = text.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

print(frequency)


# Program 29 : Reverse Sentence

text = input("\nEnter a Sentence: ")

words = text.split()

words.reverse()

print("Reversed Sentence =")

for word in words:
    print(word, end=" ")

print()


# Program 30 : String Rotation

string1 = input("\nEnter First String: ")

string2 = input("Enter Second String: ")

if len(string1) == len(string2) and string2 in (string1 + string1):
    print("Yes, It is a Rotation")
else:
    print("No, It is Not a Rotation")
