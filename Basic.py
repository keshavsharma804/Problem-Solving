# Find if a number is odd or even

a = int(input("Add number:"))
if a%2 == 0:
    print("even")
else:
    print("odd")


# Find the largest out of 3 numbers
a = int(input("Add number:"))
b = int(input("Add number:"))
c = int(input("Add number:"))
if a > b:
    print(a)
elif b > c:
    print(b)
elif c > a:
    print(c)


# Check if a string is a palindrome
a = "jack"
if a == a[::-1]:
    print("Its palindrome")
else:
    print("Its not a palindrome")


# Count vowels in a string
def count_vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = "Hello World"
print(count_vowel(s))

# Count only even digits in a string
def count_digits(d):
    count = 0
    for dig in d:
        if dig.isdigit() and int(dig)%2 == 0:
            count += 1
    return count
d = "ihaveMango456"
print(count_digits(d))


# Reverse a list without .reverse()
a = [2, 4, 6, 8, 10]
print(a[::-1])


