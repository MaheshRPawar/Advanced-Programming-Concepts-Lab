# Program 11 : Count Total Words

text = input("Enter a sentence: ")

words = text.split()

print("Total Words =", len(words))


# Program 12 : Find Longest Word

text = input("\nEnter a sentence: ")

words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word =", longest)


# Program 13 : Find Shortest Word

text = input("\nEnter a sentence: ")

words = text.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word =", shortest)


# Program 14 : Convert to Title Case

text = input("\nEnter a sentence: ")

print("Title Case =", text.title())


# Program 15 : Print Duplicate Characters

text = input("\nEnter a string: ")

printed = ""

for ch in text:

    if text.count(ch) > 1 and ch not in printed:
        print(ch)
        printed = printed + ch


# Program 16 : Frequency of Every Character

text = input("\nEnter a string: ")

checked = ""

for ch in text:

    if ch not in checked:
        print(ch, "=", text.count(ch))
        checked = checked + ch


# Program 17 : Check Anagram

string1 = input("\nEnter First String: ")
string2 = input("Enter Second String: ")

if sorted(string1) == sorted(string2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")


# Program 18 : Remove Duplicate Characters

text = input("\nEnter a string: ")

result = ""

for ch in text:

    if ch not in result:
        result = result + ch

print("Updated String =", result)


# Program 19 : Check Substring

text = input("\nEnter Main String: ")

sub = input("Enter Substring: ")

if sub in text:
    print("Substring Found")
else:
    print("Substring Not Found")


# Program 20 : Count Occurrence of a Word

text = input("\nEnter a sentence: ")

word = input("Enter Word: ")

words = text.split()

count = 0

for item in words:

    if item == word:
        count = count + 1

print("Occurrence =", count)
